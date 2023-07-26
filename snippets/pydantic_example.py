from enum import Enum, auto
import typing as t
import pydantic as pyd

from pycountry import countries


class CountrymanOrForeigner(Enum):
    COUNTRYMAN = 1
    FOREIGNER = 2


class Person(pyd.BaseModel):

    first_name: str
    last_name: str
    age: pyd.PositiveInt
    citizenship: CountrymanOrForeigner
    cash_in_wallet: t.Union[pyd.PositiveInt, pyd.PositiveFloat] = 100
    total_assets: t.Union[pyd.PositiveInt, pyd.PositiveFloat] = 100_000

    @pyd.validator("age")
    def check_max_age(cls, value): # noqa
        if value > 150:
            raise ValueError("Max allowed age is 150!")


if __name__ == "__main__":

    person1 = Person(
        first_name="John",
        last_name="Spinose",
        age=34,
        citizenship=CountrymanOrForeigner.FOREIGNER
    )
    print(f"person1 is: {person1}")

    try:
        person2 = Person(
            first_name="Mary",
            last_name="Bodenbrock",
            age=155,
            citizenship=CountrymanOrForeigner.COUNTRYMAN
        )
    except ValueError as ve:
        print(f"Caught ValueError: {ve}")

    try:
        person3 = Person(
            first_name="Valentina",
            last_name="Lacalle",
            age=27,
            citizenship=CountrymanOrForeigner.FOREIGNER,
            cash_in_wallet=1_000,
            total_assets=-100_000
        )
    except pyd.ValidationError as ve:
        print(f"Caught the following validation error: {ve}")
