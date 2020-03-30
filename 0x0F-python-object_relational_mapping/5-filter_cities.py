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

    size = cur.execute("""SELECT cities.name, states.name
                        FROM cities, states
                        WHERE cities.name IS NOT NULL
                        AND states.id = cities.state_id
                        AND states.name = 'Texas'; """)
    table = cur.fetchall()
    for entries in table:
        state = entries[1]
        if state == sys.argv[4]:
            print(entries[0])
    db.close()
