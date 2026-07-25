# python-inheritance

This project explores inheritance in Python 3: how subclasses extend and
override behavior from their parent classes, how to introspect an
object's attributes and methods, and how to check class relationships
with `isinstance`, `issubclass`, and `type`.

## Files

| File | Description |
| --- | --- |
| `0-lookup.py` | Returns the list of available attributes and methods of an object. |
| `1-my_list.py`, `tests/1-my_list.txt` | `MyList`, a `list` subclass that can print itself sorted. |
| `2-is_same_class.py` | Checks whether an object is exactly an instance of a given class. |
| `3-is_kind_of_class.py` | Checks whether an object is an instance of a class or one of its subclasses. |
| `4-inherits_from.py` | Checks whether an object's class is a strict subclass of a given class. |
| `5-base_geometry.py` | An empty `BaseGeometry` class. |
| `6-base_geometry.py` | Adds an `area()` method that raises `Exception`. |
| `7-base_geometry.py`, `tests/7-base_geometry.txt` | Adds `integer_validator()` to validate positive integers. |
| `8-rectangle.py` | `Rectangle`, a subclass of `BaseGeometry` with private, validated dimensions. |
| `9-rectangle.py` | Adds `area()` and `__str__()` to `Rectangle`. |
| `10-square.py` | `Square`, a subclass of `Rectangle`. |
| `11-square.py` | Adds its own `__str__()` to `Square`. |

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- pycodestyle 2.7.*
- No imports allowed (aside from the required `__import__()` calls)
- Every module, class, and function has a real, descriptive docstring
- Test cases live in `tests/*.txt` and run with:
  ```
  python3 -m doctest ./tests/*
  ```
