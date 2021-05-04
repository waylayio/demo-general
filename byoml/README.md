# BYOML example notebooks


These python notebooks illustrate how to use Waylay's BYOML solution.

To run these notebooks, create a [conda](https://docs.conda.io/en/latest/) 
environment corresponding to the framework you want to use.
Note that specific that the framework versions you use need to match the
ones that BYOML uses on the server.

| framework | supported version | conda env | pip requirements |
| --------- | ----------------- | -------------- | --------------------- |
| sklearn | 0.22 | [byoml_sklearn](../env/byoml_sklearn.environment.yml) | [env/byoml_sklearn.requirements.txt](../env/byoml_sklearn.requirements.txt) |
| pytorch | 1.5 | [byoml_pytorch](../env/byoml_pytorch.environment.yml) | [env/byoml_pytorch.requirements.txt](../env/byoml_pytorch.requirements.txt) | 
| tensorflow | 2.1 | [byoml_tensorflow](../env/byoml_tensorflow.environment.yml) | [env/byoml_tensorflow.requirements.txt](../env/byoml_tensorflow.requirements.txt) | 
| xgboost | 1.0 | [byoml_xgboost](../env/byoml_xgboost.environment.yml) | [env/byoml_xgboost.requirements.txt](../env/byoml_xgboost.requirements.txt) | 


```
conda env create --file env/byoml_<framework>.environment.yml
conda activate byoml_<framework>
pip install -r env/byoml_<framework>.requirements.txt
```

... and start the jupyter notebook server

```
jupyter notebook
```


