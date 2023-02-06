# BYOML example notebooks


These python notebooks illustrate how to use Waylay's BYOML solution.

To run these notebooks, create a [conda](https://docs.conda.io/en/latest/) 
environment corresponding to the framework you want to use.
Note that specific that the framework versions you use need to match the
ones that BYOML uses on the server.

See [supported runtime documentation](https://docs.waylay.io/#/api/byoml/?id=supported-runtimes)
for a complete list of currently supported runtimes and their provided dependencies.

```
conda env create --file env/byoml_<framework>/environment.yml
conda activate byoml_<framework>
pip install -r env/byoml_<framework>/requirements.txt
```

... and start the jupyter notebook server

```
jupyter notebook
```


