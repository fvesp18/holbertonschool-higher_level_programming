#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            "127.0.0.1",
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC;")
    table = cur.fetchall()
    for rows in table:
        print("{}".format(rows))
    db.close()
