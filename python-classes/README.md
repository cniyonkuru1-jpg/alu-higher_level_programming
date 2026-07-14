# Python - Classes and Object-Oriented Programming

## Description

This project introduces the fundamentals of Object-Oriented Programming (OOP) in Python through a series of tasks that progressively build a `Square` class. Each task adds a new concept — starting from a simple empty class, and building up to private attributes, property getters/setters, validation, and instance methods.

## Learning Objectives

By the end of this project, you should be able to explain, without external help:

- Why Python programming is awesome
- What is OOP
- "First-class everything"
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected, and private attributes
- What is `self`
- What is a method
- What is the Pythonic way to write getters and setters
- How to dynamically add new attributes to an existing object
- How to bind attributes to object and classes
- What is the `__init__` method and how to use it
- What is `Data Abstraction`, `Data Encapsulation`, and Information Hiding
- What is a property
- The difference between an attribute and a property in Python
- How to use the `getattr`, `setattr`, `hasattr`, and `delattr` functions

## Requirements

- Editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should follow the `pycodestyle` style guide (version 2.8.*)
- All files must be executable
- All modules should have documentation
- All classes should have documentation
- All functions (inside and outside a class) should have documentation
- No module should import anything unless explicitly authorized

## Files

| File | Description |
|---|---|
| `0-square.py` | Empty `Square` class |
| `1-square.py` | `Square` class with a private instance attribute `size` |
| `2-square.py` | `Square` class with size validation (`TypeError`/`ValueError`) |
| `3-square.py` | `Square` class with an `area()` method |
| `4-square.py` | `Square` class with `size` as a property (getter/setter) |
| `5-square.py` | `Square` class with a `my_print()` method |
| `6-square.py` | `Square` class with `size` and `position` attributes |

## Usage

Each file can be tested using its corresponding `X-main.py` test script:

```bash
$ ./0-main.py
$ ./1-main.py
$ ./2-main.py
...
```

Make sure files are executable:

```bash
$ chmod u+x *.py
```

## Example

```python
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square = Square(3, (1, 1))
my_square.my_print()
```

Output:
