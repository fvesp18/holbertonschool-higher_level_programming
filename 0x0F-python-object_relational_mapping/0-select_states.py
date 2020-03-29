#!/usr/bin/python3
""" Prints all states from a db by ascending id value """
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            "127.0.0.1",
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            3306)
    cur = db.cursor()

    size = cur.execute("SELECT * FROM states ORDER BY states.id;")
    for rows in range(size):
        products = cur.fetchone()
        print("{}".format(products))
    db.close()
