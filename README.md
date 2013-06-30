uidai
=====

Analytics on UIDAI Data released by Government of India

UIDAI Data Analytics
--------------------

This project aims to do some text analytics on Aadhaar Data released by Government of India. 

To run the project you need the following pre-requisites - 

1. Python 2.7.*
2. SQLite3

To run - 

1. First run the python file to import data from the 'csv' file to a SQLite3 DB file.

$ python csvtosqlite.py
 
2. Then use '.sql' files on the 'uidai.db' file to see the results. Purpose and output is gven in each file.
