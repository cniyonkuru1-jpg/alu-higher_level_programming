# SQL - Introduction

This project covers the basics of relational databases and SQL using MySQL 8.0.
It walks through creating and deleting databases, creating tables, and using
basic DDL and DML statements such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

## Learning Objectives

At the end of this project, I am able to explain:

- What's a database
- What's a relational database
- What does SQL stand for
- What's MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements

- All files are executed on Ubuntu 20.04 LTS using MySQL 8.0
- Every SQL query has a comment placed just before it
- Every SQL keyword is written in uppercase (`SELECT`, `WHERE`, etc.)
- Each file starts with a comment describing the task

## Files

| File | Description |
| --- | --- |
| `0-list_databases.sql` | Lists all databases of the MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if missing |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all tables of a database |
| `4-first_table.sql` | Creates the table `first_table` |
| `5-full_table.sql` | Prints the full description of `first_table` |
| `6-list_values.sql` | Lists all rows of `first_table` |
| `7-insert_value.sql` | Inserts a new row into `first_table` |
| `8-count_89.sql` | Counts records with `id = 89` in `first_table` |
| `9-full_creation.sql` | Creates `second_table` and inserts multiple rows |
| `10-top_score.sql` | Lists records of `second_table` ordered by score |
| `11-best_score.sql` | Lists records with `score >= 10` |
| `12-no_cheating.sql` | Updates Bob's score to 10 |
| `13-change_class.sql` | Removes records with `score <= 5` |
| `14-average.sql` | Computes the average score |
| `15-groups.sql` | Groups records by score, sorted by count |
| `16-no_link.sql` | Lists records that have a name, ordered by score |

## Author

Project completed as part of the ALU / Holberton higher-level programming track.
