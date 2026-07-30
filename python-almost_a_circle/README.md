# python-almost_a_circle

A project building `Rectangle` and `Square` classes on top of a shared
`Base` class, with full unit test coverage.

## Overview

- **`Base`** manages the `id` attribute for every other class, and
  provides JSON serialization / file persistence helpers
  (`to_json_string`, `from_json_string`, `save_to_file`,
  `load_from_file`, `create`).
- **`Rectangle`** inherits from `Base`, adds validated `width`,
  `height`, `x`, `y` attributes, and methods to compute area, display
  itself with `#`, update its attributes, and convert to a
  dictionary.
- **`Square`** inherits from `Rectangle`; it's a rectangle with equal
  width and height, exposed through a `size` property.

## Structure

```
models/
    __init__.py
    base.py
    rectangle.py
    square.py
tests/
    __init__.py
    test_models/
        __init__.py
        test_base.py
        test_rectangle.py
        test_square.py
```

## Requirements

- Ubuntu 20.04 LTS, python3 (version 3.8.5)
- All files start with `#!/usr/bin/python3`
- Code follows `pycodestyle` (version 2.7.*)
- All modules, classes, and methods are documented

## Running the tests

```
python3 -m unittest discover tests
```
