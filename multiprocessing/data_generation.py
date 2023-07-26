import numpy as np
import pandas as pd
import pathlib
from loguru import logger


if __name__ == "__main__":

    logger.info("Generating data...")
    X = np.random.randn(1_000_000, 10)
    y = np.dot(X, np.arange(1, 11, 1))
    X = pd.DataFrame(data=X, columns=[f"X_{i}" for i in range(1, 11, 1)])
    y = pd.DataFrame(data=y, columns=["y"])

    data = pd.concat([X, y], axis=1)

    logger.info("Saving data...")
    path = pathlib.Path(__file__).parent.parent / "data_multiprocessing" / "data_keras_example.pkl"
    logger.info(f"saving data to: {path}")
    data.to_pickle(path)
    logger.info("Data saved.")
