from snippets.make_dataset import get_default_regression_dataset
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV, KFold, train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error


n_obs = 20_000
train_share = 0.65

X, y = get_default_regression_dataset(n_obs=n_obs)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_share)


param_grid_dict = {
    "loss": ["squared_error", "absolute_error"],
    "n_estimators": [50, 100]
}

gscv = GridSearchCV(
    estimator=GradientBoostingRegressor(),
    param_grid=param_grid_dict,
    n_jobs=1,
    cv=KFold(n_splits=4),
    verbose=3,
    scoring="neg_mean_squared_error"
)

gscv.fit(X_train, y_train)

print(f"Best model: {gscv.best_params_}")
print(f"Best model type: {gscv.best_estimator_}")
y_test_predict = gscv.predict(X_test)
print(f"RMSE in test sample: {mean_squared_error(y_test, y_test_predict, squared=False):.2f}")
print(f"MAE in test sample: {mean_absolute_error(y_test, y_test_predict):.2f}")



