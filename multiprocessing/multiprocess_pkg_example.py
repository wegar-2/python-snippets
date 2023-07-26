from multiprocess import Process, Manager # noqa
import numpy as np
from loguru import logger

NUM_OF_PROCESSES = 3
NUM_OF_SAMPLES = 50


def simple_rng(process_id, size, results: dict):
    logger.info(f"Running process {process_id}...")
    np.random.seed(process_id)
    results[process_id] = np.random.randint(0, 100, size)
    logger.info(f"Process {process_id} finished!")


if __name__ == "__main__":

    manager = Manager()
    results_rng = manager.dict()

    processes_ids = list(range(0, NUM_OF_SAMPLES, 1))
    for i in range(0, NUM_OF_SAMPLES, NUM_OF_PROCESSES):

        slice_processes_ids = [k+1 for k in processes_ids[i:i+NUM_OF_PROCESSES]]
        logger.info(f"Before running processes: {', '.join([str(el) for el in slice_processes_ids])}")

        processes = []
        for j in slice_processes_ids:
            logger.info(f"Spawning process {j}...")
            p = Process(target=simple_rng, args=(j, 5, results_rng),)
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

    logger.info("Printing results: ")
    for k, v in results_rng.items():
        logger.info(f"Process {k} results: {v}")
