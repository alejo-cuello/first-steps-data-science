# Commands in console:
# mypy greeting.py # It is a static type checker
# pylint greeting.py # It is a static code analyser.Or use the VScode extension Pylint
# pycodestyle greeting.py
# pycodestyle --show-source --show-pep8 greeting.py #PEP: Python Enhancement Proposal

from typing import Iterable
from typing import Union


def greeting(name: str) -> str:
    """Function to return a greeting for a reveived name"""
    return 'Hello ' + name


greeting(3)
greeting(b'Alice')
greeting("World!")


def bad_greeting(name: str) -> str:
    """"
    This function
    is an example to get an error detected by mypy
    """
    return 'Hello ' * name


def greet_all(names: Iterable[str]) -> None:
    """This function iterates over an iterable of names, printing a greeting message for each name in the format 'Hello {name}'"""
    for name in names:
        print('Hello ' + name)


names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)
greet_all(ages)


def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return f'user-{100_000 + user_id}'
    return user_id


def nums_below(numbers: Iterable[float], limit: float) -> list[float]:
    output = []
    for num in numbers:
        if num < limit:
            output.append(num)
    return output
