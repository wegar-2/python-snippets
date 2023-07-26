from itertools import chain
from string import ascii_uppercase

# chain(iterable1, iterable2, ..., iterableN)
l1 = list(ascii_uppercase)[:10]
l2 = list(ascii_uppercase)[10:-5]
l3 = list(ascii_uppercase)[-5:]

l_res0 = list(chain(l1, l2, l3))
print(f"res0: {l_res0}")

l_res1 = list(chain.from_iterable([l1, l2, l3]))
print(f"res1: {l_res0}")

# chain: multiple iterables are passed to it, they get concatenated
# chain.from_iterable: single iterable is passed, its elements get concatenated


# References:
#   1) https://stackoverflow.com/questions/15004772/what-is-the-difference-between-chain-and-chain-from-iterable-in-itertools
