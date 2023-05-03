from time import perf_counter
import timeit


def my_sum(n=10_000_000):
    """
    Function to time, calculates sum of all natural numbers 0, 1, 2, 3, ..., N-1
    """
    s = 0
    for k in range(n):
        s += k
    return s


if __name__ == "__main__":

    # ----| Approach 1: use perf_counter --- just do two measurement for a single call of the tested function
    t0 = perf_counter()
    my_sum(100_000_000)
    print(f"Call to my_sum(100_000_000) lasted {(perf_counter() - t0):.2f} seconds")

    # ----| Approach 2: use timeit.timeit func for testing
    print(timeit.timeit(my_sum, number=10))


# References:
#   1) https://realpython.com/python-timer/#estimating-running-time-with-timeit
