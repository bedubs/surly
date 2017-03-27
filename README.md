# Single User Relational Database written in Python 3

### _Note on versioning_

Very loosely following the guidelines of [Semantic Versioning](http://semver.org/) at the most basic level.

* `MAJOR.MINOR.PATCH`

Each iteration of Surly (I and II) are minor versions, eg. `v.0.x.0`.

The final project will be the first major version, `v.1.0.0`.

_Versions will be indicated by tags._


## Surly requires Python 3.6 and Pandas

If you don't already have Python 3.6 installed, I highly recommend using the [Anaconda](https://www.continuum.io/downloads) distribution.

Anaconda comes with the conda package manager that can be used to install pandas
`conda install pandas`

If not using Anaconda, pandas can be installed using pip:
`pip install pandas`

## Basic "read-in file" program
After the requirements are met, navigate to the root of the project and run `python readin.py`. This will read in the test file and display the output in the console.

## Command Line Interface
An alternative interface is also available for command-line use. In the root directory, run `python cli.py`.

### Basic Structure of Input:
`command relation_name (optional=command specific arguments)`

### Commands:
* RELATION - Creates a relation or table
* INSERT - Insert tuple or record/values into a relation
* PRINT - Print specified item
* QUIT - Close program

### Relation
`RELATION RELATION_NAME (ATTRIBUTE_NAME ATTRIBUTE_TYPE ATTRIBUTE_LENGTH)`
ex. `RELATION MY_TABLE (Id NUM 4, NAME CHAR 20);`

### Insert

