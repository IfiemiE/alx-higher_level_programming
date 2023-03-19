#!/usr/bin/python3

""" A module demonstrating the
    the connection to a Database
    via python module 'MySQLdb'
"""

import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    psswd = sys.argv[2]
    dbase = sys.argv[3]
    myDb = MySQLdb.connect(host = 'localhost',
                            user = usr,
                            password = psswd,
                            db = dbase,
                            port = 3306)

    dbCursor = myDb.cursor()
    cities = dbCursor.execute('SELECT * FROM cities ORDER BY id')
    view_cities = dbCursor.fetchall()
    states =  dbCursor.execute('SELECT * FROM states')
    view_states = dbCursor.fetchall()
    myDb.close()
    for city_id, state_id, city in view_cities:
        for first, second in view_states:
            if state_id == first:
                state = second
                data = (city_id, city, state)
                break

        print (data)
