# SQL - More queries

This project builds on the SQL introduction by covering MySQL user privileges,
column constraints (`NOT NULL`, `DEFAULT`, `UNIQUE`), `AUTO_INCREMENT`,
`PRIMARY KEY`, `FOREIGN KEY`, subqueries, and different types of `JOIN`.

## Learning Objectives

- How to create a new MySQL user
- How to manage privileges for a user
- What's a PRIMARY KEY
- What's a FOREIGN KEY
- What's the difference between INNER, LEFT and RIGHT JOIN
- How to use UNIQUE, NOT NULL and DEFAULT constraints
- How to retrieve data from multiple tables in one request
- What are and how to use subqueries

## Requirements

- All files are executed on Ubuntu 20.04 LTS using MySQL 8.0
- Every SQL query has a comment placed just before it
- Every SQL keyword is written in uppercase (`SELECT`, `WHERE`, etc.)
- Each file starts with a comment describing the task

## Files

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists privileges of `user_0d_1` and `user_0d_2` |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges |
| `2-create_read_user.sql` | Creates `hbtn_0d_2` and a read-only user `user_0d_2` |
| `3-force_name.sql` | Creates `force_name` with a required `name` column |
| `4-never_empty.sql` | Creates `id_not_null` with a default `id` value |
| `5-unique_id.sql` | Creates `unique_id` with a unique, defaulted `id` |
| `6-states.sql` | Creates `hbtn_0d_usa` and the `states` table |
| `7-cities.sql` | Creates the `cities` table with a foreign key to `states` |
| `8-cities_of_california_subquery.sql` | Cities in California, using a subquery |
| `9-cities_by_state_join.sql` | Cities joined with their state name |
| `10-genre_id_by_show.sql` | Shows with at least one linked genre |
| `11-genre_id_all_shows.sql` | All shows with genre id, NULL if none |
| `12-no_genre.sql` | Shows without a linked genre |
| `13-count_shows_by_genre.sql` | Number of shows per genre |
| `14-my_genres.sql` | Genres linked to the show Dexter |
| `15-comedy_only.sql` | All shows in the Comedy genre |
| `16-shows_by_genre.sql` | All shows with all linked genres |

## Author

Project completed as part of the ALU / Holberton higher-level programming track.
