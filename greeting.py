# Commands in console:
# mypy greeting.py
# pylint greeting.py. Or use the VScode extension Pylint
# pycodestyle greeting.py
# pycodestyle --show-source --show-pep8 greeting.py

def greeting(name: str) -> str:
    return 'Hello ' + name


greeting(3)         # Argument 1 to "greeting" has incompatible type "int"; expected "str"
greeting(b'Alice')  # Argument 1 to "greeting" has incompatible type "bytes"; expected "str"
greeting("World!")  # No error

def bad_greeting(name: str) -> str:
    return 'Hello ' * name  # Unsupported operand types for * ("str" and "str")

def greet_all(names: list[str]) -> None:
    for name in names:
        print('Hello ' + name)

names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)   # Ok!
greet_all(ages)    # Error due to incompatible types


from collections.abc import Iterable  # or "from typing import Iterable"

def greet_all(names: Iterable[str]) -> None:
    for name in names:
        print('Hello ' + name)


from typing import Union

def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return f'user-{100_000 + user_id}'
    else:
        return user_id

def nums_below(numbers: Iterable[float], limit: float) -> list[float]:
    output = []
    for num in numbers:
        if num < limit:
            output.append(num)
    return output

