import numpy as np
import pandas as pd

# Read the data
wnba = pd.read_csv('WNBA-Player-stats-Season-2016-2017/WNBA Stats.csv')

# Get familiar with the data set.

# Top 5 rows
print(wnba.head(5))

# Bottom 5 rows
print(wnba.tail(5))

# Find the total columns and rows in the data set.
print(wnba.shape)

print(wnba.describe())
