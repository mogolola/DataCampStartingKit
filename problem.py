import os
import sys
import numpy as np
import pandas as pd
import rampwf as rw
import pickle
import gzip
from sklearn.model_selection import ShuffleSplit

problem_title = 'Crop yield prediction'
# _target_column_name = 'target'
Predictions = rw.prediction_types.make_regression()
# An object implementing the workflow
workflow = rw.workflows.FeatureExtractorRegressor()

score_types = [
    rw.score_types.RMSE(),
    rw.score_types.RelativeRMSE(name='rel_rmse'),
]



def get_cv(X, y):
    cv = ShuffleSplit(n_splits=8, test_size=0.2, random_state=57)
    return cv.split(X, y)

# --------------- X is DataFrame, y is numpy ---------------- #
def get_train_data(path='.'):

    data = np.load('./data/train.npz')

    # Shuffle
    train_X = pd.DataFrame(data['X_mean'])
    train_y = data['Y']

    return train_X, train_y



def get_test_data(path='.'):
   
    data = np.load('./data/test.npz')

    # Shuffle
    test_X = pd.DataFrame(data['X_mean'])
    test_y = data['Y']

    
    return test_X, test_y

