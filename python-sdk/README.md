# Waylay Python SDK

This section contains reference usage examples for the [Waylay Python SDK (beta)](https://pypi.org/project/waylay-beta/).

The main documentation can be found at the [Waylay Documentation Site](https://docs.waylay.io/api/sdk/python).

The current scope of the SDK is to support Data Science activities as provided by the services
* [BYOML](http://docs-io.waylay.io/#/features/byoml/)  (Machine Learning)
* [Time Series Query](http://docs-io.waylay.io/#/features/query/)
* [ETL Import](http://docs-io.waylay.io/#/features/etl/?id=etl-import-service)

This SDK is currently in beta. This implies that any subsequent version can introduce breaking changes.

# Installation

The Waylay Python SDK is available as [waylay-beta in the PyPi library repository](https://pypi.org/project/waylay-beta/).
Hence installation in a python environment (`3.6+`) just requires:

```
pip install waylay-beta
```

This will install (or use) all required dependencies such as 
[Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
but not any specific data science libraries such as [scikit-learn](https://scikit-learn.org/stable/install.html).

## Using Anaconda and Jupyter notebooks
The SDK is optimised for usage in [Jupyter Python Notebooks](https://jupyter.org/), as illustrated in this repository.

This is how you would install the SDK and interact with the examples in a [Anaconda](https://www.anaconda.com/) 
or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) environment.

```bash
# clone this repository
git clone https://github.com/waylayio/demo-general.git waylay_demo
cd waylay_demo

# create and activate new conda environment
conda create --name my_demo python=3.8
conda activate my_demo

# install the jupyter notebooks server package
conda install jupyter

# install the Waylay Python SDK
pip install waylay-beta

# install any additional tools you might need
# pip install scikit-learn

# start a notebook server (this will open a browser)
jupyter notebook
```



# API Documentation

Below is an abriged overview of the currently exposed api.
Each of the `service`.`resource`.`action` combinations correspond with a method of the Waylay Client.
```python
from waylay import WaylayClient
waylay_client = WaylayClient.from_profile()

# example WaylayClient.<service>.<resource>.<action> method
waylay_client.byoml.model.list_names()
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>method</th>
      <th>url</th>
      <th>description</th>
    </tr>
    <tr>
      <th>service</th>
      <th>resource</th>
      <th>action</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">analytics</th>
      <th rowspan="7" valign="top">query</th>
      <th>list</th>
      <td>GET</td>
      <td>/config/query</td>
      <td>List or search <em>Query Configurations</em></td>
    </tr>
    <tr>
      <th>create</th>
      <td>POST</td>
      <td>/config/query</td>
      <td>Create a new <em>Query Configuration</em></td>
    </tr>
    <tr>
      <th>get</th>
      <td>GET</td>
      <td>/config/query/{}</td>
      <td>Fetch the named <em>Query Configuration</em></td>
    </tr>
    <tr>
      <th>remove</th>
      <td>DELETE</td>
      <td>/config/query/{}</td>
      <td>Remove the named <em>Query Configuration</em></td>
    </tr>
    <tr>
      <th>replace</th>
      <td>PUT</td>
      <td>/config/query/{}</td>
      <td>Replace the named <em>Query Configuration</em></td>
    </tr>
    <tr>
      <th>data</th>
      <td>GET</td>
      <td>/data/query/{}</td>
      <td>Execute the timeseries query specified by the named <em>Query Configuration</em></td>
    </tr>
    <tr>
      <th>execute</th>
      <td>POST</td>
      <td>/data/query</td>
      <td>Execute the timeseries query specified in the request</td>
    </tr>
    <tr>
      <th>about</th>
      <th>version</th>
      <td>GET</td>
      <td>/</td>
      <td>Version info of the <em>Analytics Service</em> at this endpoint.</td>
    </tr>
    <tr>
      <th rowspan="11" valign="top">byoml</th>
      <th rowspan="10" valign="top">model</th>
      <th>list</th>
      <td>GET</td>
      <td>/models</td>
      <td>List the metadata of the deployed <em>BYOML Models</em></td>
    </tr>
    <tr>
      <th>list_names</th>
      <td>GET</td>
      <td>/models</td>
      <td>List the names of deployed <em>BYOML Models</em></td>
    </tr>
    <tr>
      <th>create</th>
      <td>POST</td>
      <td>/models</td>
      <td>Build and create a new <em>BYOML Model</em> as specified in the request</td>
    </tr>
    <tr>
      <th>replace</th>
      <td>PUT</td>
      <td>/models/{}</td>
      <td>Build and replace the named <em>BYOML Model</em></td>
    </tr>
    <tr>
      <th>get</th>
      <td>GET</td>
      <td>/models/{}</td>
      <td>Fetch the metadata of the named <em>BYOML Model</em></td>
    </tr>
    <tr>
      <th>examples</th>
      <td>GET</td>
      <td>/models/{}/examples</td>
      <td>Fetch the <em>example request input</em> of the named <em>BYOML Model</em></td>
    </tr>
    <tr>
      <th>predict</th>
      <td>POST</td>
      <td>/models/{}/predict</td>
      <td>Execute the <em>predict</em> capability of the named <em>BYOML Model</em></td>
    </tr>
    <tr>
      <th>regress</th>
      <td>POST</td>
      <td>/models/{}/regress</td>
      <td>Execute the <em>regress</em> capability of the named  <em>BYOML Model</em></td>
    </tr>
    <tr>
      <th>classify</th>
      <td>POST</td>
      <td>/models/{}/classify</td>
      <td>Execute the <em>classification</em> capability of the named <em>BYOML Model</em></td>
    </tr>
    <tr>
      <th>remove</th>
      <td>DELETE</td>
      <td>/models/{}</td>
      <td>Remove the named <em>BYOML Model</em></td>
    </tr>
    <tr>
      <th>about</th>
      <th>health</th>
      <td>GET</td>
      <td>/</td>
      <td>Get the health status of the <em>BYOML Service</em></td>
    </tr>
  </tbody>
</table>
