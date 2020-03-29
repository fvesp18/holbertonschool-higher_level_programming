#!/usr/bin/python3
""" Prints all states from a db by ascending id value """
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="127.0.0.1",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states;")
    table = cur.fetchall()
    for row in table:
        print("{}".format(row))
    db.close()
