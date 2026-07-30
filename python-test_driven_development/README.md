# python-test_driven_development

Introduction to Python Programming and Databases — Test-driven development.

This project focuses on writing documentation and tests **before**
implementing functions, and covers `doctest` and `unittest`.

## Learning Objectives

- Why Python programming is awesome
- What's an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Requirements

- Ubuntu 20.04 LTS, python3 (version 3.8.5)
- All files start with `#!/usr/bin/python3`
- All files end with a new line
- Code follows `pycodestyle` (version 2.7.*)
- All modules and functions are documented
- All files are executable

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-add_integer.py` | Adds two integers |
| 1 | `2-matrix_divided.py` | Divides all elements of a matrix |
| 2 | `3-say_my_name.py` | Prints `My name is <first name> <last name>` |
| 3 | `4-print_square.py` | Prints a square with `#` |
| 4 | `5-text_indentation.py` | Prints text with indentation after `.`, `?`, `:` |
| 5 | `6-max_integer.py` | Finds the max integer in a list (with `unittest`) |

## Running the tests

Doctests:

```
python3 -m doctest ./tests/*.txt
```

Unittest:

```
python3 -m unittest tests.6-max_integer_test
```
