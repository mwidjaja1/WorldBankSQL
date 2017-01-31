# -*- coding: utf-8 -*-
"""
Example of loading SQL Database via Pandas and doing calculations in Python
"""

import pandas as pd
import sqlite3

con = sqlite3.connect('factbook.db')
query = 'SELECT * from facts'
data = pd.read_sql_query(query, con)

print(data['area_land'].sum() / data['area_water'].sum())