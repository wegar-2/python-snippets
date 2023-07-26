import numpy as np
from loguru import logger
from multiprocessing import Pool


NUM_OF_PROCESSES = 3
NUM_OF_SAMPLES = 50


def simple_rng(data_dict: dict):
    process_id = data_dict.get("process_id")
    size = data_dict.get("size")
    logger.info(f"Running process {process_id}...")
    np.random.seed(process_id)
    return np.random.randint(0, 100, size)


if __name__ == "__main__":

    args_vec = [{
        "process_id": k, "size": 5
    } for k in range(1, NUM_OF_SAMPLES+1, 1)]

    with Pool(NUM_OF_PROCESSES) as pool:
        results = pool.map(simple_rng, args_vec)

    logger.info(f"Printing results: ")
    for result in results:
        logger.info(f"{result}")

    logger.info("Done!")
