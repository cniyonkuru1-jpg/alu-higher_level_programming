## Description

This project is a deep dive into Python object-oriented programming,
focused on building a `Rectangle` class incrementally across 10 tasks.
Each file builds on the one before it, adding new features step by step:
private attributes, property getters/setters, custom string
representations, instance counting, static and class methods.

## Learning Objectives

By the end of this project, the following concepts are covered:

- Why Python programming is awesome
- How to build a class in Python
- The purpose of private and public attributes/methods in a class
- The difference between a private attribute and a "protected" one
- How to define getters and setters for a class using the `@property`
  decorator
- The Pythonic way to write getters and setters
- How to dynamically add/remove new attributes to an object
- How to bind an attribute to an object
- What `**kwargs` is and how to use it
- How to use `__dict__`
- What a static method is and when to use one
- What a class method is and when to use one
- How to detect the deletion of an instance using `__del__`
- How to use `eval()` to recreate an instance from its `repr()`

## Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Code should follow the PEP8 style guide (`pycodestyle`)
- All files must be executable
- No modules may be imported unless explicitly stated in the task

## Files

| File            | Description                                                        |
|-----------------|---------------------------------------------------------------------|
| `0-rectangle.py`| An empty `Rectangle` class                                          |
| `1-rectangle.py`| `Rectangle` with private `width`/`height` and property accessors    |
| `2-rectangle.py`| Adds `area()` and `perimeter()` methods                             |
| `3-rectangle.py`| Adds `__str__` for a printable rectangle shape                      |
| `4-rectangle.py`| Adds `__repr__` so instances can be recreated with `eval()`         |
| `5-rectangle.py`| Adds `__del__` to print a message on instance deletion              |
| `6-rectangle.py`| Adds `number_of_instances` class attribute to track live instances  |
| `7-rectangle.py`| Adds `print_symbol` class attribute for custom string output        |
| `8-rectangle.py`| Adds `bigger_or_equal()` static method to compare two rectangles    |
| `9-rectangle.py`| Adds `square()` class method to create a Rectangle with equal sides |

## Usage

Each file can be imported and tested independently, for example:
