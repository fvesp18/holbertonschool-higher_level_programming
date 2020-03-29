#!/usr/bin/python3
""" Prints all states from a db by ascending id value """
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            "localhost",
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            3306
            )
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id;")
    table = cur.fetchall()
    for rows in table:
        print("{}".format(rows))
    db.close()
