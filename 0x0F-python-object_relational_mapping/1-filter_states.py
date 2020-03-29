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

    size = cur.execute("SELECT * FROM states;")
    for rows in range(size):
        result = cur.fetchone()
        string = result[1]
        string = string[:1]
        if string == 'N':
            print("{}".format(result))
    db.close()
