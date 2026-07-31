#!/usr/bin/python3
"""Script that lists all states matching a user-provided name.

This version builds the query with str.format, which makes it
vulnerable to SQL injection (see 3-my_safe_filter_states.py for the
safe version).
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = db.cursor()
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' "
        "ORDER BY id ASC").format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
