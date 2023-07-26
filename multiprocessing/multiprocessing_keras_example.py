import typing as t
from itertools import chain
from loguru import logger
import numpy as np
import pandas as pd
import pathlib
from multiprocessing import Pool

NUM_OF_PROCESSES = 4


def get_data(n: int = 10_000, seed: int = 12345):
    logger.info("Loading data...")
    data = pd.read_pickle(pathlib.Path(__file__).parent.parent / "data" / "data_keras_example.pkl")
    X, y = data.drop("y", axis=1), data["y"]
    logger.info("Data loaded. Returning loaded data.")
    np.random.seed(seed)
    rows = np.random.choice(range(X.shape[0]), n, replace=False)
    return X.values[rows], y.values[rows]


def create_network(nns: t.List[int]):
    from keras.layers import Dense
    from keras import Sequential
    layers = [Dense(nn, "relu") for nn in nns] + [Dense(1, "linear")]
    network = Sequential(layers)
    network.compile(optimizer="adam", loss="binary_crossentropy", metrics=["mse"])
    return network


def get_networks_layers():
    two_layers = [(i, j) for i in range(3, 6) for j in range(1, i+1)]
    three_layers = [(i, j, k) for i in range(3, 5) for j in range(1, i+1) for k in range(1, j+1)]
    return list(chain(two_layers, three_layers))


def fit_network(data_dict: dict):

    nns = data_dict["nns"]
    network_id = data_dict["network_id"]
    X = data_dict["X"]
    y = data_dict["y"]

    logger.info(f"Fitting network with layers: {', '.join([str(el) for el in nns])}")
    network = create_network(nns)
    np.random.seed(network_id*1000)
    network.fit(X, y, batch_size=128, epochs=1, verbose=1)
    return {"layers": nns, "evaluation_metrics": network.evaluate(X, y)}


if __name__ == "__main__":

    logger.info("Loading data for parallelized run using multiprocess...")
    X, y = get_data()

    logger.info("Retrieving networks' layers...")
    networks_layers = get_networks_layers()
    logger.info(f"Num of networks: {len(networks_layers)}")

    list_of_args = [
        {"nns": nns, "X": X, "y": y, "network_id": network_id + 1}
        for network_id, nns in enumerate(networks_layers)
    ]

    with Pool(processes=NUM_OF_PROCESSES) as pool:
        results = pool.map(fit_network, list_of_args)

    logger.info("All processes finished. Printing results...")
    for ix, el in enumerate(results):
        logger.info(f"Result {ix}: {el}")
