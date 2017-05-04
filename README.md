___
### _SURLY 3 Requirements_

_Build upon SURLY 2 and implement the SURLY commands below (see SURLY spec)._  
_The `WHERE` clause of `DELETE` and `SELECT` should handle multiple conditions._

* `DELETE WHERE`
* `SELECT`
* `JOIN`

Use the implemented commands to build 5 interesting queries that involve 2 
or more relations. Continue working in teams of 2 using the data model you
designed earlier in the semester. 

Program functionality must be demonstrated 
to the instructor before the due date. 

Deliverables to be submitted include:

* source code (submit build and share Git repository on CsGit)
* a hard-copy and digital report (in this format)
* test input file (including the above queries) and corresponding output

#### Example Commands:

* `DELETE PREREQ WHERE CNUM1 = CS2510 or CNUM1 = CS3510 and CNUM2 != CS1510;`
* `SELECT COURSE WHERE CNUM = CS2510 and CREDITS > 3;`
* `T1 = SELECT COURSE WHERE CNUM = CS2510;`
* `PRINT T1;`
* `J = JOIN COURSE, PREREQ ON CNUM = CNUM2;`
* `S = SELECT J WHERE CNUM = CS2510;`
* `PRINT S;`
___

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
After the requirements are met, navigate to the root of the project and run `python readin.py`.
This will read in a file and display the output in the console.
The program will close on completion.

## Command Line Interface
An alternative interface is also available for command-line use.
In the root directory, run `python cli.py`.
This starts the program with a command prompt that allows user to enter commands.

Running this command with an optional filepath will run the script to build the 
database and relations, and remain open as a command prompt for further operations.

ex. `python cli.py data/pizzeria_data.txt`

### Basic Structure of Input:
`command relation_name (optional=command specific arguments)`

### Commands:
* RELATION - Creates a relation or table
* INSERT - Insert tuple or record/values into a relation
* PRINT - Print specified item
* DELETE - Delete the contents of a relation
* DESTROY - Remove a relation from the database
* PROJECT - Specify columns from a relation to store in a new temporary relation.
* QUIT/EXIT - Close program

### Relation

`RELATION RELATION_NAME (ATTRIBUTE_NAME ATTRIBUTE_TYPE ATTRIBUTE_LENGTH)`

ex. `RELATION MY_TABLE (Id NUM 4, NAME CHAR 20);`

### Insert

`INSERT RELATION_NAME ATTRIBUTE_1 ATTRIBUTE_2 ATTRIBUTE_3...;`

ex. `INSERT MY_TABLE 4095 Hector;`

### PRINT

`PRINT RELATION_NAME;`

ex. `PRINT MY_TABLE;`

_SPECIAL PRINT:_ `PRINT CATALOG;` _WILL PRINT THE DATABASE CATALOG/STRUCTURE._

### DELETE

`DELETE RELATION_NAME;`

### DESTROY

`DESTROY RELATION_NAME;`

### PROJECT

`PROJECT attribute1, attribute2 FROM RELATION_NAME;`

### QUIT

`QUIT` or `EXIT` will close the program if running CLI 
