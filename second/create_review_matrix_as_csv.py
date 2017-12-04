#!/usr/bin/env/python
"""Creating review matrix as csv"""

import pandas as pd
import numpy as np

# Read the dataset into a data table using Pandas
DF = pd.read_csv("movie_ratings_data_set.csv")

# Convert the running list of our user ratings into a matrix using the 'pivot table' function
RATINGS_DF = pd.pivot_table(DF, index='user_id', columns='movie_id', aggfunc=np.max)

#Create a csv file of the data for easy viewing
RATINGS_DF.to_csv("review_matrixx.csv", na_rep="")
