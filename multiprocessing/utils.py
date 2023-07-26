import pandas as pd
import pathlib
from loguru import logger


def get_data():
    logger.info("Loading data...")
    data = pd.read_pickle(pathlib.Path(__file__).parent.parent / "data" / "data_keras_example.pkl")
    X, y = data.drop("y", axis=1), data["y"]
    logger.info("Data loaded. Returning loaded data.")
    return X.values, y.values
