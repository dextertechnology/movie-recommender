#!/usr/bin/env/python
"""Make recommendation of movie according to the rating"""

import pandas as pd
import numpy as np
import matrix_factorization_utilities

# Load user ratings
RAW_DATASET_DF = pd.read_csv('movie_ratings_data_set.csv')

# Convert the running list of user ratings into a matrix
RATINGS_DF = pd.pivot_table(RAW_DATASET_DF, index='user_id', columns='movie_id', aggfunc=np.max)

# Apply matrix factorization to find the latent features
U, M = matrix_factorization_utilities.low_rank_matrix_factorization(
    RATINGS_DF.as_matrix(),
    num_features=15,
    regularization_amount=0.1
)

# Find all predicted ratings by multiplying the U by M
PREDICTED_RATINGS = np.matmul(U, M)

# Save all the ratings to a csv file
PREDICTED_RATINGS_DF = pd.DataFrame(
    index=RATINGS_DF.index,
    columns=RATINGS_DF.columns,
    data=PREDICTED_RATINGS
)
PREDICTED_RATINGS_DF.to_csv("predicted_ratings.csv")
