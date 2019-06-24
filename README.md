Lemmatizer - Python - Indonesian
==========

This is a port to python of Indonesian lemmatizer created by David Christiandy and his friends, originally for his webapp in php.



Thanks to David Christiandy and his friends that originally created this, and my friends Sadhu and Joshua for doing most of the work.



Running the demo
------------

* Import `database/db_lemmatizer.sql` to your MySQL database

* Default configuration for MySQL:

  ```
  host: localhost
  user: root
  pass: <none>
  database: lemmatizer
  ```
  You can also change it if you want, just remember to change the configuration in lemmatizer.py

* Install pcre in your system. In Debian/Ubuntu-based systems, install with ```apt-get install libpcre3 libpcre3-dev```. In MacOS, install with homebrew ```brew install pcre```.

* Install several python packages:
  ```
  pip install mysql-connector-python
  pip install python-pcre
  pip install nltk (required for the demo in main.py)
  ```
  
* Run main.py



Database
--------

The database consists of 3 tables: `dictionary`, `result`, and `word`.