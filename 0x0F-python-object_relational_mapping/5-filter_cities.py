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
    print(', '.join([city[0] for city in table]))
    db.close()
