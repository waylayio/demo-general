from pathlib import Path
import statsmodels.tsa.statespace.sarimax as sm
import numpy as np
import json
import math

SEASONAL_ORDER = (1, 1, 1, 24)
ORDER = (1, 1, 1)
MAX_ITER = 250
ALPHA = 0.05
DEFAULT_PATH = Path("model.json")


class SarimaWeatherModel:
    order: (int, int, int)
    seasonal_order: (int, int, int, int)
    params: np.ndarray | None = None

    def __init__(self, order=None, seasonal_order=None, params=None, predict_window=24):
        self.order = order or ORDER
        self.seasonal_order = seasonal_order or SEASONAL_ORDER
        self.params = np.array(params) if params is not None else None
        self.predict_window = predict_window

    def to_dict(self):
        return dict(
            order=self.order,
            seasonal_order=self.seasonal_order,
            params=self.params.tolist() if self.params is not None else None,
        )

    @classmethod
    def load(cls, location: Path = DEFAULT_PATH):
        """Load the model."""
        with open(location, encoding="utf-8") as f:
            return cls(**json.load(f))

    def save(self, location: Path = DEFAULT_PATH):
        """Save the model."""
        with open(location, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f)

    def endo_exog(self, data: np.ndarray, exog=None):
        """If no explicit exog is given, assume first feature is endog..."""
        if exog is not None:
            return (data, exog)
        if len(data.shape) == 1:
            return (data, None)
        if data.shape[0] == 1:
            return (data.flatten(), None)
        return (data[:, 0], data[:, 1:])

    def train(self, data: np.ndarray, exog=None, **kwargs):
        if self.params is not None:
            raise TypeError("already fitted")
        model = self._fitted_model(data, exog, **kwargs)
        self.params = model.params
        return model

    def predict(
        self,
        data,
        exog=None,
        start: int | None = None,
        end: int | None = None,
        dynamic=None,
        alpha=None,
    ):
        if self.params is None:
            raise TypeError("not fitted")
        exog_fit, exog_pred = None, None
        if exog is not None:
            exog_fit = exog[: data.size]
            if end is None:
                end = exog.shape[0]
            exog_pred = exog[data.size - 1 : end]
        endog_fit, exog_fit = self.endo_exog(data, exog_fit)
        fitted = self._fitted_model(endog_fit, exog_fit)
        start = start or -self.predict_window
        dynamic = dynamic or start != 0
        pred = fitted.get_prediction(
            start=start, dynamic=dynamic, end=end, exog=exog_pred
        )
        if alpha:
            return pred.conf_int(alpha=alpha)
        return pred.predicted_mean

    def _fitted_model(self, data, exog=None, **fit_kwargs):
        endog, exog = self.endo_exog(data, exog)
        model = sm.SARIMAX(
            endog, exog=exog, order=self.order, seasonal_order=self.seasonal_order
        )
        if self.params is not None:
            return model.smooth(self.params)
        return model.fit(maxiter=MAX_ITER, **fit_kwargs)

    def __call__(
        self,
        data,
        exog=None,
        start=None,
        end=None,
        dynamic=None,
        alpha=None,
    ):
        return self.predict(
            data,
            exog,
            start=as_value(start),
            end=as_value(end),
            dynamic=dynamic,
            alpha=as_value(alpha),
        )


def as_value(val_or_numpy):
    if isinstance(val_or_numpy, np.ndarray):
        return val_or_numpy.tolist()
    return val_or_numpy
