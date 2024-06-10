# ML-adapter demo notebooks

These notebooks demonstrate the Waylay _Machine Learning Adapters_ feature that bring your 
machine learning models into the Waylay ecosystem as _waylay plug_ or _waylay webscript_.

## prerequisites
* access to a Waylay system. You'll need a
    * waylay gateway endpoint (e.g. `https://api.waylay.io` for the enterprise deployment)
    * an api key/secret pair (e.g. via **> Settings > Authentication Keys** in the [Waylay Console](https://console.waylay.io/administration/settings/keys))
* a python 3.11 environment. The examples here will assume you use [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) and run
  the python notebooks locally. But you alternatively can use a [python 3.11 venv](https://docs.python.org/3/library/venv.html), or a remote notebook server
  provided e.g. by [Google Colab](https://colab.research.google.com/) or [Kaggle](https://www.kaggle.com).

## Run a notebook (conda scripted)

You can use the [scripts](../bin) and [predefined environments](../env) in this repository to set up a _conda_ environment with the required dependencies (if not yet present),
and start a notebook server.

E.g. to start the a notebook server for the [torch_autoencoder](ml_adapter/torch_autoencoder) demo, using 
the environment settings in [env/ml_adapter_torch](env/ml_adapter_torch), 
use the following in a command line at the root of this repository:
```
bin/jupyter_notebook env/ml_adapter_torch ml_adapter/torch_autoencoder
```

## Environment creation (conda manual)
Alternatively, to manually create a conda environment (e.g. named `my_torch_demo`), follow the following steps:
```
conda create -n my_torch_demo python=3.11
conda activate my_torch_demo
conda install jupyterlab
```
Use separate environments with other names if you have models that require different dependencies.

Install the required dependencies:

#### The `ml-adapter` library of choice

Installs the package to initialize and run a ml model in a _plug_ or _webscript_.
These package are released on [pypi](https://pypi.org/search/?q=waylay-ml-adapter).
The exact package depends on the ML framework you use (see demo notebooks), currently available:

* `waylay-ml-adapter-numpy` for generic models that use numpy data representation
* `waylay-ml-adapter-sklearn` for scikit-learn models.
* `waylay-ml-adapter-torch` for pytorch models.

```
pip install waylay-ml-adapter-torch
```

#### The `waylay-sdk` with the sdk plugin for _ml adapters_
Installs the _python sdk_ to interact with the waylay system, and activates an sdk extension to support the creation
and testing of _ml adapter_ webscripts and plugs.
Uses the package released on [pypi](https://pypi.org/search/?q=waylay-sdk).

```
pip install waylay-ml-adapter-sdk
```

The first time you'll use the python sdk, a prompt will request you and endpoint
and credentials for the waylay system.

#### Other dependencies
Some demos require additional dependencies mentioned in the notebook itself.
E.g. if you need to serialize models with _dill_: 
```
pip install dill
```

#### Language server (optional)
This enables some more auto-completion support in the jupyter notebooks.
```
pip install jedi-language-server
```


#### Start the notebook server
Starts a local notebook server that you can interact with through a browser.
```
jupyter lab
```
