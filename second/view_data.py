#!/usr/bin/env python
"""Read csv file and write in html"""

import webbrowser
import os
import pandas

# Read dataset from csv using pandas
DATA_TABLE = pandas.read_csv("movie_ratings_data_set.csv")

# Create a web page view of the data for easy viewing
HTML = DATA_TABLE[0:100].to_html()

# Save the html to a html formatted file
with open("data.html", "w") as f:
    f.write(HTML)

# Open directly when script run using webbrowser
FULL_FILENAME = os.path.abspath("data.html")
webbrowser.open("file://{}".format(FULL_FILENAME))
