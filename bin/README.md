# utility scripts

This folder contains example utility scripts to manage conda environments and 
render notebooks to html and markdown in batch.

## [conda_create](conda_create)

`conda_create <env-name>` 

Creates the conda environment with the given name. The files
```
/env/<env-name>/environment.yml
/env/<env-name>/requirement.txt 
```
should exist.

## [jupyter_notebook](jupyter_notebook)
`jupyter_notebook <env-name> [<notebook-file>]`

Starts a jupyter notebook server running in the given conda environment. 
The conda environment will be created from the files in [/env](../env) if it does not exist.
Optionally, the `notebook-file` will be opened.

## [render_notebook](render_notebook)

`render_notebook <env-name> <notebook-file>`

Renders the jupyter notebook `notebook-file` in the given conda environment as follows:
* creates the conda environment if it doesn't exists, and config files in [/env](../env) are found.
* uses [papermill](https://papermill.readthedocs.io/en/latest/) to execute the notebook, and puts the resulting notebook in the folder `$EXEC_OUT` (default `./output/exec`)
* converts the executed notebook to html to folder `$HTML_OUT` (default `./output/html`) 
* converts the executed notebook to markdown to folder `$MARKDOWN_OUT` (default `./output/markdown`). Any cell tagged with `doc_exclude` will be excluded from this rendering.

## [conda_remove](conda_remove)

`conda_remove <env-name>` 

removes the conda environment with the given name.

