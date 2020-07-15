# Databases with Python
Parsing xml and json data and storing it in SQLite databases using Python

## Overview
The two python files database_xml.py and database_json.py use XML and JSON data respectively, parse and clean it and then store the data into the two sqlite databases present in
the repository, namely tracks.sqlite and roster2.sqlite. These databases can be viewed and edited using MySQL or by using the DB Browser computer application, which can be downloaded 
from this [link](https://sqlitebrowser.org/dl/).

The Python library **sqlite3** is used for creating and manipulating the databases.

## About the Data
The data used is available as a part of the Python for Everybody Specialization ([link](https://www.coursera.org/specializations/python?skipBrowseRedirect=true)) provided by the 
University of Michigan on [Coursera](https://coursera.org).

The XML data is available as Library.xml and the Json data is available as roster_data.json in the repository.

## How to Use
1. Download the data from the repository and set the folder containing the downloaded data as the working directory. 

2. Make sure you have all the libraries used in the two python files. In case you need to download any of the libraries, use this command on your Command Prompt:
```
pip install 'your library name'
```

3. Once you have all the libraries imported, copy the code from database_xml.py or database_json.py and run it.



