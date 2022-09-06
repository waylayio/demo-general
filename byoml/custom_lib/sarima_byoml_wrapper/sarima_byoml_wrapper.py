"""BYOML Model wrappers for Sarima models"""
import numpy as np
import pandas as pd
import statsmodels.api as sm

def convert_to_pandas(data, feature_columns=['value'], index_freq='QS'):
    """convert data with as first feature epoch-milliseconds."""
    expected_row_size = 1 + len(feature_columns)
    if isinstance(data, list):
        data = np.array(data)
    if isinstance(data, np.ndarray):
        (instance_count, row_count) = data.shape
        if row_count == expected_row_size:
            timestamps = data[:,0] 
            values = data[:, 1:]              
        elif instance_count == expected_row_size:
            # support both column and row-oriented array shapes
            timestamps = data[0,:]
            values = data[1:, :].transpose()
        else:
            raise ValueError(f"This model requires a timestamp and '{feature_columns}' rows as input")
        if len(timestamps) and isinstance(timestamps[0], np.number):
            # millisecond epoch is standard for waylay
            timestamp_index = pd.to_datetime(timestamps, unit='ms')
        else:
            # this will parse ISO8601 timestamp strings
            timestamp_index = pd.to_datetime(timestamps)
        if index_freq:
            timestamp_index.freq=index_freq
        data = pd.DataFrame(values, index=timestamp_index, columns=feature_columns)

    if not isinstance(data, pd.DataFrame):
        raise ValueError('This model requires an input that can be converted to a dataframe.')
        
    return data

def convert_to_numpy(series_or_df):
    # convert dataframe to an array of (timestamp_millis, value) tuples
    timestamps = series_or_df.index.map(lambda _ : _.timestamp() * 1000).values
    if isinstance(series_or_df, pd.DataFrame):
        df = series_or_df
        series = [ df[c].values for c in df.columns ]
        return np.array([timestamps, *series]).transpose()
    else:
        series = series_or_df.values
        return np.array([timestamps, series]).transpose()

class SARIMAXForecaster:
    def __init__(self, window=24):
        self.window = window
        self.fitted_params = None

    def map_input(self, request):
        """Convert the json-data request payload to the input for `predict`."""
        return convert_to_pandas(request['instances'])
    
    def map_output(self, request, result):
        """Convert the output of `predict` to a json-data response payload."""
        return { 'predictions': convert_to_numpy(result).tolist() }

    def create_model(self, data):
        return sm.tsa.SARIMAX(
            data,
            seasonal_order=(1, 1, 1, 4),
            order=(1, 0, 0),
            trend=[1, 0, 0],
            enforce_stationarity=False
        )
    
    def fit(self, data, **fit_args):
        fitted_model = self.create_model(data).fit(**fit_args)
        self.fitted_params = fitted_model.params
        return fitted_model
    
    def get_fitted_model(self, data):
        model = self.create_model(data)
        if self.fitted_params is None:
            raise ValueError('Model has not been fitted')
        return model.smooth(self.fitted_params)
        
    def predict(self, data):
        fitted_model = self.get_fitted_model(data)
        return fitted_model.forecast(steps=self.window)



class SARIMAXConfidenceForecaster(SARIMAXForecaster):
    def __init__(self, window=24, default_alpha=0.05):
        super().__init__(window)
        self.default_alpha = default_alpha
        
    def map_input(self, request):
        # allow the user to specify an alternate alpha for the confidence intervals
        alpha = request.get('alpha', self.default_alpha)
        return (
            super().map_input(request),
            alpha
        )
        
    def predict(self, data_and_alpha):
        data, alpha = data_and_alpha
        fitted_model = self.get_fitted_model(data)
        forecast = fitted_model.get_forecast(steps=self.window)
        return forecast.conf_int(alpha)