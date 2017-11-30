#!/usr/bin/env python
"""Read csv file and write in html"""

import webbrowser
import os
import pandas

# Read dataset from csv using pandas and set one of the column as index
DATA_TABLE = pandas.read_csv("movies.csv", index_col="movie_id")

# Create a web page view of the data for easy viewing
HTML = DATA_TABLE.to_html()

# Save the html to a html formatted file
with open("movie_list.html", "w") as f:
    f.write(HTML)

# Open directly when script run using webbrowser
FULL_FILENAME = os.path.abspath("movie_list.html")
webbrowser.open("file://{}".format(FULL_FILENAME))
