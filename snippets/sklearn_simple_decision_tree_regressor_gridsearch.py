import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from snippets.make_dataset import get_default_regression_dataset

n_obs=10_000
train_set_share = 0.75
X, y = get_default_regression_dataset(n_obs=n_obs)

# --------- split into train and test datasets manually ---------
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, train_size=int(n_obs * train_set_share), random_state=12345)

# --------- perform GridSearchCV on linear regression ---------
param_grid_dec_tree = {
    "criterion": ["squared_error", "absolute_error"],
    "max_depth": [2, 5, 10, 20]
}
gs_cv = GridSearchCV(
    estimator=DecisionTreeRegressor(),
    n_jobs=4,
    refit=True,
    cv=3,
    param_grid=param_grid_dec_tree
)
print("starting fitting...")
gs_cv.fit(X=X_train, y=y_train)
print("done fitting...")

print(f"Best estimator: {gs_cv.best_estimator_}")
print(f"Best estimator's params: {gs_cv.best_params_}")
y_test_predict = gs_cv.predict(X_test)
print(f"RMSE: {np.sqrt(mean_squared_error(y_true=y_test, y_pred=y_test_predict)):.2f}")
print(f"MAE: {mean_absolute_error(y_true=y_test, y_pred=y_test_predict):.2f}")
