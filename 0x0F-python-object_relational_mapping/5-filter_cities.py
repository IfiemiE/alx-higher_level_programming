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
    stat = sys.argv[4]
    for i in stat:
        if i == ';':
            stat = None
    if stat is not None:
        myDb = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=usr,
                               password=psswd,
                               db=dbase)

        dbCursor = myDb.cursor()
        cities = dbCursor.execute(f"SELECT c.name\
                                   FROM cities AS c\
                                   INNER JOIN states as s\
                                   WHERE (c.state_id = s.id)\
                                   AND (s.name = '{stat}')\
                                   ORDER BY c.id")
        view_cities = dbCursor.fetchall()
        if len(view_cities) == 0:
            print(" ")
        else:
            for i in range(len(view_cities)):
                if i == (len(view_cities) - 1):
                    print(view_cities[i][0])
                else:
                    print(view_cities[i][0], end=", ")
