import typing as t
from multiprocess import Process, Manager # noqa
from itertools import chain
from loguru import logger
import numpy as np
import pandas as pd
import pathlib

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
    network.compile(optimizer="adam", loss="mse", metrics=["mse"])
    return network


def get_networks_layers():
    two_layers = [(i, j) for i in range(3, 6) for j in range(1, i+1)]
    three_layers = [(i, j, k) for i in range(3, 5) for j in range(1, i+1) for k in range(1, j+1)]
    return list(chain(two_layers, three_layers))


def fit_network(nns: t.List[int], results_dict: dict, network_id: int):
    logger.info(f"Fitting network with layers: {', '.join([str(el) for el in nns])}")
    network = create_network(nns)
    np.random.seed(network_id*1000)
    network.fit(X, y, batch_size=128, epochs=1, verbose=1)
    results_dict[network_id] = network.evaluate(X, y)
    logger.info(f"Network evaluation: {results_dict[network_id]}")


if __name__ == "__main__":

    logger.info("Loading data for parallelized run using multiprocess...")
    X, y = get_data()

    logger.info("Retrieving networks' layers...")
    networks_layers = get_networks_layers()
    logger.info(f"Num of networks: {len(networks_layers)}")

    manager = Manager()
    results_dict = manager.dict()

    for i in range(0, len(networks_layers), NUM_OF_PROCESSES):

        networks_layers_slice = networks_layers[i:i+NUM_OF_PROCESSES]
        ids = [id_ + 1 for id_ in range(i, min([i+NUM_OF_PROCESSES, len(networks_layers)]))]

        logger.info(f"Processing ids: {ids}")
        processes = []
        for j in range(NUM_OF_PROCESSES):
            p = Process(target=fit_network, args=(networks_layers_slice[j], results_dict, ids[j]))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

    logger.info("All processes finished. Printing results...")
    for k, v in results_dict.items():
        logger.info(f"Network {k} results: {v}")
