import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error


# --------- script meta parameters ---------
n_obs = 10_000
train_set_share = 0.75


# --------- prepare the datset ---------
X, y = make_regression(
    n_samples=n_obs,
    n_features=20,
    n_informative=10,
    n_targets=1,
    bias=50,
    noise=10
)

# --------- split into train and test datasets manually ---------
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, train_size=int(n_obs * train_set_share), random_state=12345)

# --------- split into train and test datasets manually ---------

