import typing as t

import numpy as np
from sklearn.datasets import make_regression


def get_default_regression_dataset(n_obs: int = 100_000) -> t.Tuple[np.array, np.array]:
    return make_regression(
        n_samples=n_obs,
        n_features=20,
        n_informative=10,
        n_targets=1,
        bias=50,
        noise=10
    )
