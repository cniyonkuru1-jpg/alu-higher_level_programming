# python-everything_is_object

In Python, everything is an object: integers, strings, lists, functions,
even classes themselves. This project explores what that really means —
object identity vs. equality, mutable vs. immutable types, how variables
reference objects, and how arguments are passed to functions.

## Files

| File | Description |
| --- | --- |
| `0-answer.txt` | Function used to print an object's type. |
| `1-answer.txt` | Function used to get an object's identifier (memory address). |
| `2-answer.txt` – `5-answer.txt` | Whether two int variables point to the same object. |
| `6-answer.txt` – `13-answer.txt` | Output of `==` and `is` comparisons for strings and lists. |
| `14-answer.txt` – `18-answer.txt` | Output of scripts illustrating aliasing, function argument passing, and mutability. |
| `19-copy_list.py` | A 3-line function that returns a shallow copy of a list without importing any module. |
| `20-answer.txt` – `28-answer.txt` | Questions about tuples, identity, and in-place vs. rebinding operations. |

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- pycodestyle 2.7.*
- Answer files (`.txt`) contain a single line, no shebang
- Python files start with `#!/usr/bin/python3`, end with a newline, and are
  executable
- No imports allowed in `19-copy_list.py`
