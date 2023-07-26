from enum import Enum, auto
from pycountry import countries

# create dictionary of countries
# countries_dict = {val_.name.upper(): key_ for key_, val_ in enumerate(list(countries))}

countries_names = [el.name for el in list(countries)]

# create CountryEnum class from dict
CountryEnum = Enum(
    "CountryEnum",
    countries_names
)
print([c for c in CountryEnum])
dir(CountryEnum)
# x = CountryEnum