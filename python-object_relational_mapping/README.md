# python-object_relational_mapping

Connecting Python to a MySQL database, first with raw SQL via
`MySQLdb`, then through an ORM using `SQLAlchemy`.

## Part 1: MySQLdb

| File | Description |
|---|---|
| `0-select_states.py` | Lists all states, sorted by id |
| `1-filter_states.py` | Lists states whose name starts with uppercase `N` |
| `2-my_filter_states.py` | Lists states matching a user-provided name (built with `str.format`, **vulnerable to SQL injection** — see task 3) |
| `3-my_safe_filter_states.py` | Same as above, but safe from SQL injection via a parameterized query |
| `4-cities_by_state.py` | Lists all cities with their state, via a single `JOIN` query |
| `5-filter_cities.py` | Lists cities of a given state, safe from SQL injection |

## Part 2: SQLAlchemy (ORM)

| File | Description |
|---|---|
| `model_state.py` | `State` model, mapped to the `states` table |
| `model_city.py` | `City` model, mapped to the `cities` table, with a foreign key to `states.id` |
| `6-model_state.py` | Creates the `states` table from the `State` model |
| `7-model_state_fetch_all.py` | Lists all `State` objects |
| `8-model_state_fetch_first.py` | Prints the first `State` object (by id), without fetching the whole table |
| `9-model_state_filter_a.py` | Lists `State` objects whose name contains `a` |
| `10-model_state_my_get.py` | Prints the id of the `State` matching a given name |
| `11-model_state_insert.py` | Adds a new `State` named "Louisiana" |
| `12-model_state_update_id_2.py` | Renames the `State` with id 2 to "New Mexico" |
| `13-model_state_delete_a.py` | Deletes all `State` objects whose name contains `a` |
| `14-model_city_fetch_by_state.py` | Lists all `City` objects grouped by state |

## Requirements

- Ubuntu 20.04 LTS, python3 (version 3.8.5)
- `MySQLdb` version 2.0.x, `SQLAlchemy` version 1.4.x
- All files start with `#!/usr/bin/python3`
- Code follows `pycodestyle` (version 2.7.*)
- All modules, classes, and functions are documented
- Scripts do nothing when imported (guarded by `if __name__ == "__main__":`)

## Usage

Every script connecting to MySQL takes the username, password, and
database name as its first three arguments (plus a search term for
some scripts):

```
./0-select_states.py <mysql_username> <mysql_password> <database_name>
```
