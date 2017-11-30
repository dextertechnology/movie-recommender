#!/usr/bin/env python
"""Read csv file and write in html"""

import webbrowser
import os
import pandas as pd
import numpy as np

# Read dataset from csv using pandas
DATA_TABLE = pd.read_csv("movie_ratings_data_set.csv")

# Convert the running list of user ratings into a matrix using the 'pivot table' function
RATINGS_DF = pd.pivot_table(DATA_TABLE, index='user_id', columns='movie_id', aggfunc=np.max)

# Create a web page view of the data for easy viewing
HTML = RATINGS_DF.to_html(na_rep="")

# Save the html to a html formatted file
with open("review_matrix.html", "w") as f:
    f.write(HTML)

# Open directly when script run using webbrowser
FULL_FILENAME = os.path.abspath("review_matrix.html")
webbrowser.open("file://{}".format(FULL_FILENAME))
