# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 07:24:20 2023

@author: jmayu
"""

#Purpose: Query database using SQL

#   Run BuildWeatherDB.py to build weather database before running this program

import sqlite3
import pandas as pd


#file names for database and output file
dbFile = "weather.db"

#format output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

#connect to and query weather database 
conn = sqlite3.connect(dbFile)
#Create SQL command
selectCmd = " SELECT * FROM observations order by timestamp; "
                
                
#print out the query
result = pd.read_sql_query(selectCmd, conn)
print(result)
