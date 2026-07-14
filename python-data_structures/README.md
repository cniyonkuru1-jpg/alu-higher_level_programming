# Python - Data Structures

## Description

This project covers the fundamentals of Python's core data structures — lists, tuples, and matrices — through a series of tasks that build functions to manipulate them without relying on many of Python's built-in shortcuts. The goal is to understand how these structures work "under the hood" by implementing common operations manually.

## Learning Objectives

By the end of this project, you should be able to explain, without external help:

- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What is a mutable object versus an immutable object
- What is a list, how to use it, what are lists most common methods
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What are the sequence types in Python
- What is a mapping type in Python
- Compound data types
- How to use `str.format()`

## Requirements

- Editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should follow the `pycodestyle` style guide (version 2.8.*)
- All files must be executable
- All modules should have documentation
- All functions should have documentation
- No module should import anything unless explicitly authorized

## Files

| File | Description |
|---|---|
| `0-print_list_integer.py` | Prints all integers of a list |
| `1-element_at.py` | Retrieves an element from a list, C-style |
| `2-replace_in_list.py` | Replaces an element in a list at a specific position |
| `3-print_reversed_list_integer.py` | Prints all integers of a list, in reverse |
| `4-new_in_list.py` | Replaces an element in a copy of a list, without modifying the original |
| `5-no_c.py` | Removes all `c` and `C` characters from a string |
| `6-print_matrix_integer.py` | Prints a matrix of integers |
| `7-add_tuple.py` | Adds two tuples together |
| `8-multiple_returns.py` | Returns the length and first character of a string |
| `9-max_integer.py` | Finds the biggest integer in a list |
| `10-divisible_by_2.py` | Checks which elements of a list are divisible by 2 |
| `11-delete_at.py` | Deletes an item at a specific position in a list |
| `12-switch.py` | Switches the values of two variables |

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
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
```

Output:
