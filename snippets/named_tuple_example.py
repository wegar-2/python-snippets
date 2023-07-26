from collections import namedtuple
from itertools import product

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor

# define namedtuple
GridPoint = namedtuple(
    typename="GridPoint",
    field_names=[
        "max_num_indep_vars",
        "search_method",
        "model_class",
    ]
)


if __name__ == "__main__":

    # create and print tons of instances of namedtuple
    l_max_num_indep_vars = [5, 10, 15, 17]
    l_search_method = ["forward", "backward"]
    l_model_class = [LinearRegression, GradientBoostingRegressor, KNeighborsRegressor]

    l_grid = [GridPoint(*el) for el in list(product(l_max_num_indep_vars, l_search_method, l_model_class))]
    for key, point in enumerate(l_grid):
        print(f"point #{key}: {point}")

x = 123
y = 0
z = 123.33

if x:
    print(x)
if y:
    print(x)
if z:
    print(z)
