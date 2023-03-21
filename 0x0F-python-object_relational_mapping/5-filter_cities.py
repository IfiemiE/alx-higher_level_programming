#!/usr/bin/python3

""" A module demonstrating the
    the connection to a Database
    via python module 'MySQLdb'
"""

import MySQLdb
import sys

def filter_cities(state):
    """filter_cities: prints out cities in a given state
        Args:
            state (str): The given state
        Returns:The query for the selection
    """
    query = f"SELECT c.name\
            FROM cities AS c\
            INNER JOIN states AS s\
            WHERE s.name = '{state}' AND c.state_id = s.id\
            ORDER BY c.id"

    return (query)

if __name__ == '__main__':
    usr = sys.argv[1]
    psswd = sys.argv[2]
    dbase = sys.argv[3]
    ns = sys.argv[4]
    for p in range(len(ns)):
        if (ns[p] == ';'):
            ns = None
    if ns != None:
        myDb = MySQLdb.connect(host = 'localhost',
                                user = usr,
                                password = psswd,
                                db = dbase,
                                port = 3306)
        dbCursor = myDb.cursor()

        Query = filter_cities(ns)
        dbCursor.execute(Query)
        view = dbCursor.fetchall()
        dbCursor.close()
        myDb.close()
        count = 0
        if len(view) != 0:
            for c in view:
                count += 1
                if count != len(view):
                    print (c[0], end=', ')
                else:
                    print(c[0])

        else:
            print(" ")
