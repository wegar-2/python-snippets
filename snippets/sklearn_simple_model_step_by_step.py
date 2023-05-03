from collections import namedtuple

import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression


# ============================================================================================================
# ============================ DESCRIPTION OF THIS CASE STUDY ================================================

# ============================================================================================================


# --------- 1. prepare the data set to use ---------
X, y = make_regression(
    n_samples=200_000,
    n_features=20,
    n_targets=1,
    random_state=567890
)

# --------- 2. define points on a grid search ---------
GridPoint = namedtuple(
    typename="GridPoint",
    field_names=[
        "train_set_share",
        "model_search_method"
    ]
)

