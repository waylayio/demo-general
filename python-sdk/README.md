# Waylay Python SDK

This section contains reference usage examples for the [Waylay Python SDK (beta)](https://pypi.org/project/waylay-beta/).

The main documentation can be found at the [Waylay Documentation Site](https://docs.waylay.io/api/sdk/python).

The SDK currently supports Data Science activities as provided by the Waylay features
* [BYOML](http://docs-io.waylay.io/#/features/byoml/)  (Machine Learning)
* [Time Series Query](http://docs-io.waylay.io/#/features/query/) (definition of aggregated data sets)
* [ETL](http://docs-io.waylay.io/#/features/etl/?id=etl-import-service) (Bulk import of timeseries data)

This SDK is currently in beta. This implies that any subsequent version can introduce breaking changes.

# Installation

The Waylay Python SDK is available as [waylay-beta in the PyPi library repository](https://pypi.org/project/waylay-beta/).
Hence installation in a python environment (`3.6+`) just requires:

```
pip install waylay-beta
```

This will install (or re-use) required dependencies such as 
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

# Notebooks

Example notebooks are available for the following categories

* [byoml](byoml/) deploy your Machine Learning models on the waylay platform.
* [general](general/) general features of the Python SDK
* [query](query/) define and execute time series queries
* [etl_import](etl_import/) bulk import your csv files and pandas dataframes into Waylay

## Plotting
Some of the demo notebooks uses the [pandas basic plotting](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#basic-plotting-plot)
integration. This will require the additional dependency
```
pip install matplotlib
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
      <td>List or search <em>Query Configurations</em>.<br><a href="https://docs.waylay.io/api/query/search/#search" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/query/?id=data-query-search-api" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>create</th>
      <td>POST</td>
      <td>/config/query</td>
      <td>Create a new <em>Query Configuration</em>.<br><a href="https://docs.waylay.io/api/query/crud/#create" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/query/?id=create" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>get</th>
      <td>GET</td>
      <td>/config/query/{}</td>
      <td>Fetch the named <em>Query Configuration</em>.<br><a href="https://docs.waylay.io/api/query/crud/#retrieve" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/query/?id=retrieve" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>remove</th>
      <td>DELETE</td>
      <td>/config/query/{}</td>
      <td>Remove the named <em>Query Configuration</em>.<br><a href="https://docs.waylay.io/api/query/crud/#delete" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/query/?id=delete" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>replace</th>
      <td>PUT</td>
      <td>/config/query/{}</td>
      <td>Replace the named <em>Query Configuration</em>.<br><a href="https://docs.waylay.io/api/query/crud/#replace" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/query/?id=replace" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>data</th>
      <td>GET</td>
      <td>/data/query/{}</td>
      <td>Execute the timeseries query specified by the named <em>Query Configuration</em>.<br><a href="https://docs.waylay.io/api/query/data/#query-execution" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/query/?id=query-execution" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>execute</th>
      <td>POST</td>
      <td>/data/query</td>
      <td>Execute the timeseries query specified in the request body.<br><a href="https://docs.waylay.io/api/query/data/#query-execution" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/query/?id=query-execution" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>about</th>
      <th>version</th>
      <td>GET</td>
      <td>/</td>
      <td>Version info of the <em>Analytics Service</em> at this endpoint.<br></td>
    </tr>
    <tr>
      <th rowspan="12" valign="top">byoml</th>
      <th rowspan="11" valign="top">model</th>
      <th>list</th>
      <td>GET</td>
      <td>/models</td>
      <td>List the metadata of the deployed <em>BYOML Models</em><br><a href="https://docs.waylay.io/api/byoml/#overview-of-the-api" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/byoml/?id=overview-of-the-api" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>list_names</th>
      <td>GET</td>
      <td>/models</td>
      <td>List the names of deployed <em>BYOML Models</em><br><a href="https://docs.waylay.io/api/byoml/#overview-of-the-api" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/byoml/?id=overview-of-the-api" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>create</th>
      <td>POST</td>
      <td>/models</td>
      <td>Build and create a new <em>BYOML Model</em> as specified in the request<br><a href="https://docs.waylay.io/api/byoml/#how-to-upload-your-model" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/byoml/?id=how-to-upload-your-model" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>replace</th>
      <td>PUT</td>
      <td>/models/{}</td>
      <td>Build and replace the named <em>BYOML Model</em><br><a href="https://docs.waylay.io/api/byoml/#overwriting-a-model" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/byoml/?id=overwriting-a-model" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>get</th>
      <td>GET</td>
      <td>/models/{}</td>
      <td>Fetch the metadata of the named <em>BYOML Model</em><br><a href="https://docs.waylay.io/api/byoml/#checking-out-your-model" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/byoml/?id=checking-out-your-model" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>get_content</th>
      <td>GET</td>
      <td>/models/{}/content</td>
      <td>Fetch the content of the named <em>BYOML Model</em><br><a href="https://docs.waylay.io/api/byoml/#checking-out-your-model" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/byoml/?id=checking-out-your-model" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>examples</th>
      <td>GET</td>
      <td>/models/{}/examples</td>
      <td>Fetch the <em>example request input</em> of the named <em>BYOML Model</em><br><a href="https://docs.waylay.io/api/byoml/#example-input" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/byoml/?id=example-input" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>predict</th>
      <td>POST</td>
      <td>/models/{}/predict</td>
      <td>Execute the <em>predict</em> capability of the named <em>BYOML Model</em><br><a href="https://docs.waylay.io/api/byoml/#predictions" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/byoml/?id=predictions" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>regress</th>
      <td>POST</td>
      <td>/models/{}/regress</td>
      <td>Execute the <em>regress</em> capability of the named  <em>BYOML Model</em><br><a href="https://docs.waylay.io/api/byoml/#predictions" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/byoml/?id=predictions" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>classify</th>
      <td>POST</td>
      <td>/models/{}/classify</td>
      <td>Execute the <em>classification</em> capability of the named <em>BYOML Model</em><br><a href="https://docs.waylay.io/api/byoml/#predictions" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/byoml/?id=predictions" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>remove</th>
      <td>DELETE</td>
      <td>/models/{}</td>
      <td>Remove the named <em>BYOML Model</em><br><a href="https://docs.waylay.io/api/byoml/#deleting-a-model" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/byoml/?id=deleting-a-model" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>about</th>
      <th>health</th>
      <td>GET</td>
      <td>/</td>
      <td>Get the health status of the <em>BYOML Service</em><br></td>
    </tr>
    <tr>
      <th rowspan="13" valign="top">api</th>
      <th>settings</th>
      <th>get</th>
      <td>GET</td>
      <td>/api/settings</td>
      <td>Retrieve tenant global settings.<br></td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">resource</th>
      <th>get</th>
      <td>GET</td>
      <td>/api/resources/{}</td>
      <td>Retrieve a `resource` representation.<br><a href="https://docs.waylay.io/api/resources/#retrieve-resource" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=retrieve-resource" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>create</th>
      <td>POST</td>
      <td>/api/resources</td>
      <td>Create a `resource` entity.<br><a href="https://docs.waylay.io/api/resources/#create-resource" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=create-resource" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>update</th>
      <td>PATCH</td>
      <td>/api/resources/{}</td>
      <td>(Partially) update a `resource` representation.<br><a href="https://docs.waylay.io/api/resources/#partial-resource-update" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=partial-resource-update" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>replace</th>
      <td>PUT</td>
      <td>/api/resources/{}</td>
      <td>Replace a `resource` representation.<br><a href="https://docs.waylay.io/api/resources/#update-resource" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=update-resource" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>remove</th>
      <td>DELETE</td>
      <td>/api/resources/{}</td>
      <td>Delete a `resource` entity.<br><a href="https://docs.waylay.io/api/resources/#delete-resource" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=delete-resource" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>search</th>
      <td>GET</td>
      <td>/api/resources</td>
      <td>Query `resource` entities.<br><a href="https://docs.waylay.io/api/resources/#query-resources" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=query-resources" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">resource_type</th>
      <th>create</th>
      <td>POST</td>
      <td>/api/resourcetypes</td>
      <td>Create a `resource type` entity.<br><a href="https://docs.waylay.io/api/resources/#create-resource-type" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=create-resource-type" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>remove</th>
      <td>DELETE</td>
      <td>/api/resourcetypes/{}</td>
      <td>Delete a `resource type` entity.<br><a href="https://docs.waylay.io/api/resources/#delete-resource-type" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=delete-resource-type" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>replace</th>
      <td>PUT</td>
      <td>/api/resourcetypes/{}</td>
      <td>Replace a `resource type` representation.<br><a href="https://docs.waylay.io/api/resources/#update-resource-type" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=update-resource-type" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>update</th>
      <td>PATCH</td>
      <td>/api/resourcetypes/{}</td>
      <td>(Partially) update a `resource type` representation.<br><a href="https://docs.waylay.io/api/resources/#partial-resource-type-update" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=partial-resource-type-update" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>get</th>
      <td>GET</td>
      <td>/api/resourcetypes/{}</td>
      <td>Retrieve a `resource type` representation.<br><a href="https://docs.waylay.io/api/resources/#retrieve-resource-type" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=retrieve-resource-type" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>list</th>
      <td>GET</td>
      <td>/api/resourcetypes</td>
      <td>Query `resource type` entities.<br><a href="https://docs.waylay.io/api/resources/#query-resource-types" target="_doc">doc</a> | <a href="https://docs-io.waylay.io/#/api/resources/?id=query-resource-types" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th rowspan="20" valign="top">storage</th>
      <th rowspan="2" valign="top">bucket</th>
      <th>list</th>
      <td>GET</td>
      <td>/bucket</td>
      <td>List available bucket aliases<br><a href="https://docs-io.waylay.io/#/api/storage/?id=list-bucket" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>get</th>
      <td>GET</td>
      <td>/bucket/{}</td>
      <td>Get metadata for a specific bucket alias<br><a href="https://docs-io.waylay.io/#/api/storage/?id=get-bucket" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">object</th>
      <th>sign_get</th>
      <td>GET</td>
      <td>/bucket/{}/{}?sign=GET</td>
      <td>Create a signed http GET link for the given bucket and object path.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=sign_url" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>sign_post</th>
      <td>GET</td>
      <td>/bucket/{}/{}?sign=POST</td>
      <td>Create a signed http POST link for the given bucket and object path.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=sign_url" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>sign_put</th>
      <td>GET</td>
      <td>/bucket/{}/{}?sign=PUT</td>
      <td>Create a signed http PUT link for the given bucket and object path.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=sign_url" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>stat</th>
      <td>GET</td>
      <td>/bucket/{}/{}?stat=true</td>
      <td>Get the object metadata for the given bucket and object path.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=get-object" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>remove</th>
      <td>DELETE</td>
      <td>/bucket/{}/{}</td>
      <td>Remove the object at the given bucket and object path.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=delete-object-or-folder" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>list</th>
      <td>GET</td>
      <td>/bucket/{}/{}</td>
      <td>List objects in given bucket with a given path prefix.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=list-object" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">folder</th>
      <th>list</th>
      <td>GET</td>
      <td>/bucket/{}/{}/</td>
      <td>List objects in this folder.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=list-object" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>create</th>
      <td>PUT</td>
      <td>/bucket/{}/{}/</td>
      <td>Create a folder.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=put-folder" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>stat</th>
      <td>GET</td>
      <td>/bucket/{}/{}/?stat=true</td>
      <td>Get the details of this folder<br><a href="https://docs-io.waylay.io/#/api/storage/?id=get-object" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>remove</th>
      <td>DELETE</td>
      <td>/bucket/{}/{}/</td>
      <td>Remove this folder<br><a href="https://docs-io.waylay.io/#/api/storage/?id=delete-object-or-folder" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">subscription</th>
      <th>list</th>
      <td>GET</td>
      <td>/subscription/{}</td>
      <td>List available subscriptions for a given bucket.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=list-bucket-subscriptions" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>get</th>
      <td>GET</td>
      <td>/subscription/{}/{}</td>
      <td>Retrieve the representation of a notification subscription.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=get-subscription" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>create</th>
      <td>POST</td>
      <td>/subscription/{}</td>
      <td>Create a new notification subscription.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=create-subscription" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>replace</th>
      <td>PUT</td>
      <td>/subscription/{}/{}</td>
      <td>Create or Replace the definition of a notification subscription.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=update-subscription" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>remove</th>
      <td>DELETE</td>
      <td>/subscription/{}/{}</td>
      <td>Remove a notification subscription.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=delete-subscription" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>remove_all</th>
      <td>DELETE</td>
      <td>/subscription/{}</td>
      <td>Remove all notification subscription that satisfy a query.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=delete-subscriptions" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">about</th>
      <th>version</th>
      <td>GET</td>
      <td>/</td>
      <td>Application version<br><a href="https://docs-io.waylay.io/#/api/storage/?id=version" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>status</th>
      <td>GET</td>
      <td>/status</td>
      <td>Validation and statistics on the buckets and policies for this tenant.<br><a href="https://docs-io.waylay.io/#/api/storage/?id=tenant-status" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">etl</th>
      <th rowspan="2" valign="top">etl_import</th>
      <th>initiate</th>
      <td>POST</td>
      <td>/api/etl/import</td>
      <td>Initiates an etl import process as specified in the request body.<br><a href="https://docs-io.waylay.io/#/features/etl/?id=etl-import-service" target="_iodoc">iodoc</a></td>
    </tr>
    <tr>
      <th>get</th>
      <td>GET</td>
      <td>/api/etl/import</td>
      <td>Retrieves the last or active etl import process.<br><a href="https://docs-io.waylay.io/#/features/etl/?id=etl-import-service" target="_iodoc">iodoc</a></td>
    </tr>
  </tbody>
</table>

