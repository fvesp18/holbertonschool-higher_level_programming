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

    size = cur.execute("SELECT * FROM states;")
    for rows in range(size):
        products = cur.fetchone()
        print("{}".format(products))
    db.close()
