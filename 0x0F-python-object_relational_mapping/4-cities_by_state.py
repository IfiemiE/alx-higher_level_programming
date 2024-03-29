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
    myDb = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=usr,
                           password=psswd,
                           db=dbase)

    dbCursor = myDb.cursor()
    cities = dbCursor.execute('SELECT c.id, c.name, s.name\
                               FROM cities AS c\
                               INNER JOIN states as s\
                               WHERE c.state_id = s.id\
                               ORDER BY c.id')
    view_cities = dbCursor.fetchall()
    for v in view_cities:
        print(v)
