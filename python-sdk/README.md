# Waylay Python SDK

This section contains reference usage examples for the [Waylay Python SDK (beta)](https://pypi.org/project/waylay-beta/).

The main documentation can be found at the [Waylay Documentation Site](https://docs.waylay.io/api/sdk/python).

The SDK currently supports Data Science activities as provided by the Waylay features
* [BYOML](http://docs.waylay.io/#/features/byoml/)  (Machine Learning)
* [Time Series Query](http://docs.waylay.io/#/features/query/) (definition of aggregated data sets)
* [ETL](http://docs.waylay.io/#/features/etl/?id=etl-import-service) (Bulk import of timeseries data)

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
  <tr>
    <th>service</th>
    <th>resource</th>
    <th>action</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
    <tr>
      <th rowspan="18" valign="top">byoml</th>
      <th rowspan="11" valign="top">model</th>
      <th>list</th>
      <td><div>List the metadata of the deployed <em>BYOML Models</em></div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=overview-of-the-api" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>list_names</th>
      <td><div>List the names of deployed <em>BYOML Models</em></div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=overview-of-the-api" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>upload</th>
      <td><div>Upload a new machine learning model with given name, framework and description.</div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=how-to-upload-your-model" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>replace</th>
      <td><div>Replace a machine learning model with given name, framework and description.</div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=overwriting-a-model" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>get</th>
      <td><div>Fetch the metadata of the named <em>BYOML Model</em></div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=checking-out-your-model" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>update</th>
      <td><div>Update the metadata of the named <em>BYOML Model</em>.
Only metadata attributes can be modified.</div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=update-metadata-for-a-model" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>examples</th>
      <td><div>Fetch the <em>example request input</em> of the named <em>BYOML Model</em></div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=example-input" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>predict</th>
      <td><div>Execute the <em>predict</em> capability of the named <em>BYOML Model</em></div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=predictions" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>regress</th>
      <td><div>Execute the <em>regress</em> capability of the named  <em>BYOML Model</em></div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=predictions" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>classify</th>
      <td><div>Execute the <em>classification</em> capability of the named <em>BYOML Model</em></div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=predictions" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>remove</th>
      <td><div>Remove the named <em>BYOML Model</em></div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=deleting-a-model" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>about</th>
      <th>health</th>
      <td><div>Get the health status of the <em>BYOML Service</em></div></td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">framework</th>
      <th>list</th>
      <td><div>Frameworks and supported runtimes.</div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=runtimes" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>get</th>
      <td><div>Get the default runtime for a framework.</div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=runtimes" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>list_versions</th>
      <td><div>Get the runtimes for a framework.</div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=runtimes" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>get_version</th>
      <td><div>Get the runtime for a given framework and framework version.</div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=runtimes" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">runtime</th>
      <th>list</th>
      <td><div>List runtimes (framework and framework version).</div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=runtimes" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>get</th>
      <td><div>Get a supported runtime.</div>
<div><a href="https://docs.waylay.io/#/api/byoml/?id=runtimes" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th rowspan="11" valign="top">timeseries</th>
      <th rowspan="11" valign="top">etl_tool</th>
      <th>prepare_import</th>
      <td><div>Convert an input data set to a locally stored timeseries file.</div></td>
    </tr>
    <tr>
      <th>initiate_import</th>
      <td><div>Upload a prepared timeseries file to the etl-import ingestion bucket.</div></td>
    </tr>
    <tr>
      <th>list_import</th>
      <td><div>List all imports in all states on the `etl-import` bucket.</div></td>
    </tr>
    <tr>
      <th>check_import</th>
      <td><div>Validate the status of an import process started by this tool.</div></td>
    </tr>
    <tr>
      <th>cleanup_import</th>
      <td><div>Clean up the server storage for an import task.</div></td>
    </tr>
    <tr>
      <th>read_import_as_csv</th>
      <td><div>Read an etl import file as a csv stream.</div></td>
    </tr>
    <tr>
      <th>read_import_as_dataframe</th>
      <td><div>Read an etl import file as pandas dataframe.</div></td>
    </tr>
    <tr>
      <th>list_import_resources</th>
      <td><div>List resource and metric metadata contained in an ETL import file.</div></td>
    </tr>
    <tr>
      <th>update_resources</th>
      <td><div>Create or update the Waylay Resources for the timeseries in this dataset.</div></td>
    </tr>
    <tr>
      <th>export_series_as_csv</th>
      <td><div>Export a number of series from the times series database.</div></td>
    </tr>
    <tr>
      <th>update_query</th>
      <td><div>Create or update a waylay query containing all the series defined in this import.</div></td>
    </tr>
    <tr>
      <th rowspan="7" valign="top">queries</th>
      <th rowspan="6" valign="top">query</th>
      <th>list</th>
      <td><div>List the names of stored queries. <br>Use filter like <code>params=dict(q="name:demo")</code> to filter the listing. <br>Use <code>select_path=["queries"]</code> to return the query entities rather than names. </div>
<div><a href="https://docs.waylay.io/#/api/query/?id=data-query-search-api" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>create</th>
      <td><div>Store a new query definition under a name. Fails if a query already exist with that name.</div>
<div><a href="https://docs.waylay.io/#/api/query/?id=create" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>get</th>
      <td><div>Get the named query definition.</div>
<div><a href="https://docs.waylay.io/#/api/query/?id=retrieve" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>remove</th>
      <td><div>Remove the named query definition.</div>
<div><a href="https://docs.waylay.io/#/api/query/?id=delete" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>replace</th>
      <td><div>Create or replace the named query defition.</div>
<div><a href="https://docs.waylay.io/#/api/query/?id=replace" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>execute</th>
      <td><div>Execute a timeseries query by name (string) or definition (object).</div>
<div><a href="https://docs.waylay.io/#/api/query/?id=query-execution" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>about</th>
      <th>version</th>
      <td><div>Version info of the <em>Queries Service</em> at this endpoint.</div></td>
    </tr>
    <tr>
      <th rowspan="12" valign="top">resources</th>
      <th rowspan="6" valign="top">resource</th>
      <th>get</th>
      <td><div>Retrieve a `resource` representation.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=retrieve-resource" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>create</th>
      <td><div>Create a `resource` entity.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=create-resource" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>update</th>
      <td><div>(Partially) update a `resource` representation.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=partial-resource-update" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>replace</th>
      <td><div>Replace a `resource` representation.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=update-resource" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>remove</th>
      <td><div>Delete a `resource` entity.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=delete-resource" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>list</th>
      <td><div>Query `resource` entities.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=query-resources" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">resource_type</th>
      <th>create</th>
      <td><div>Create a `resource type` entity.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=create-resource-type" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>remove</th>
      <td><div>Delete a `resource type` entity.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=delete-resource-type" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>replace</th>
      <td><div>Replace a `resource type` representation.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=update-resource-type" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>update</th>
      <td><div>(Partially) update a `resource type` representation.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=partial-resource-type-update" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>get</th>
      <td><div>Retrieve a `resource type` representation.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=retrieve-resource-type" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>list</th>
      <td><div>Query `resource type` entities.</div>
<div><a href="https://docs.waylay.io/#/api/resources/?id=query-resource-types" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th rowspan="23" valign="top">storage</th>
      <th rowspan="2" valign="top">bucket</th>
      <th>list</th>
      <td><div>List available bucket aliases</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=list-bucket" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>get</th>
      <td><div>Get metadata for a specific bucket alias</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=get-bucket" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th rowspan="7" valign="top">object</th>
      <th>sign_get</th>
      <td><div>Create a signed http GET link for the given bucket and object path.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=sign_url" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>sign_post</th>
      <td><div>Create a signed http POST link for the given bucket and object path.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=sign_url" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>sign_put</th>
      <td><div>Create a signed http PUT link for the given bucket and object path.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=sign_url" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>stat</th>
      <td><div>Get the object metadata for the given bucket and object path.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=get-object" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>remove</th>
      <td><div>Remove the object at the given bucket and object path.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=delete-object-or-folder" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>list</th>
      <td><div>List objects in given bucket with a given path prefix.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=list-object" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>iter_list_all</th>
      <td><div>Use paging to iterate over all objects.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=list-object" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">folder</th>
      <th>list</th>
      <td><div>List objects in this folder.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=list-object" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>create</th>
      <td><div>Create a folder.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=put-folder" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>stat</th>
      <td><div>Get the details of this folder</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=get-object" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>remove</th>
      <td><div>Remove this folder</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=delete-object-or-folder" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">subscription</th>
      <th>list</th>
      <td><div>List available subscriptions for a given bucket.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=list-bucket-subscriptions" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>get</th>
      <td><div>Retrieve the representation of a notification subscription.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=get-subscription" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>create</th>
      <td><div>Create a new notification subscription.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=create-subscription" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>replace</th>
      <td><div>Create or Replace the definition of a notification subscription.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=update-subscription" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>remove</th>
      <td><div>Remove a notification subscription.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=delete-subscription" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>remove_all</th>
      <td><div>Remove all notification subscription that satisfy a query.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=delete-subscriptions" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">about</th>
      <th>version</th>
      <td><div>Application version</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=version" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>status</th>
      <td><div>Validation and statistics on the buckets and policies for this tenant.</div>
<div><a href="https://docs.waylay.io/#/api/storage/?id=tenant-status" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">content</th>
      <th>put</th>
      <td><div>Retrieve the content of a storage object.</div></td>
    </tr>
    <tr>
      <th>get</th>
      <td><div>Retrieve the content of a storage object.</div></td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">util</th>
      <th rowspan="2" valign="top">info</th>
      <th>action_info_df</th>
      <td><div>Produce a pandas DataFrame with an overview of the provided actions.</div></td>
    </tr>
    <tr>
      <th>action_info_html</th>
      <td><div>Render the service/resource/action listing as an html table.</div></td>
    </tr>
    <tr>
      <th>etl</th>
      <th>etl_import</th>
      <th>get</th>
      <td><div>Retrieves the last or active etl import process.</div>
<div><a href="https://docs.waylay.io/#/features/etl/?id=etl-import-service" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">data</th>
      <th rowspan="5" valign="top">series</th>
      <th>data</th>
      <td><div>Retrieve the (optionally aggregated) data of a single series.</div>
<div><a href="https://docs.waylay.io/#/api/broker/?id=getting-time-series-data" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>list</th>
      <td><div>Retrieve a list of series and their latest value for a given resource.</div>
<div><a href="https://docs.waylay.io/#/api/broker/?id=metadata" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>latest</th>
      <td><div>Fetch the latest value for a series.</div>
<div><a href="https://docs.waylay.io/#/api/broker/?id=latest-value-for-a-series" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>query</th>
      <td><div>Execute a broker query document to retrieve aggregated timeseries.</div>
<div><a href="https://docs.waylay.io/#/api/broker/?id=post-timeseries-query" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>export</th>
      <td><div>Export a single series using paging with HAL links.</div>
<div><a href="https://docs.waylay.io/#/api/broker/?id=getting-time-series-data" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">events</th>
      <th>post</th>
      <td><div>Forward a json message to the rule engine, time series database and/or document store for a given resource.</div>
<div><a href="https://docs.waylay.io/#/api/broker/?id=posting-data-to-the-storage-and-rule-engine" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>bulk</th>
      <td><div>Forward an array of json messages to the rule engine, time series database and/or document store.</div>
<div><a href="https://docs.waylay.io/#/api/broker/?id=posting-array-of-data" target="_doc">doc</a></div></td>
    </tr>
    <tr>
      <th>remove</th>
      <td><div>Remove all data for a resource.</div>
<div><a href="https://docs.waylay.io/#/api/broker/?id=all-data-for-a-resource" target="_doc">doc</a></div></td>
    </tr>
  </tbody>
</table>


