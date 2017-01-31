# -*- coding: utf-8 -*-
"""
Example of loading SQL Database via Pandas and doing processing & calculations
in Python
"""

import math
import pandas as pd
import sqlite3


def final_population(row):
    """ Calculates final population """
    initial_pop = row['population']
    pop_growth = row['population_growth']
    return initial_pop * (math.e ** (pop_growth * 35))


con = sqlite3.connect('factbook.db')
query = 'SELECT * from facts'
data = pd.read_sql_query(query, con)

# Clean Data
data = data.dropna()

# Calculates final population and returns the top 10 with largest population
data['final_population'] = data.apply(final_population, axis=1)
print(data.sort_values('final_population', ascending=False)['name'][:10])
