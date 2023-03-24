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
    myDb = MySQLdb.connect(host='localhost', port=3306,
                           user=usr, password=psswd, db=dbase)

    dbCursor = myDb.cursor()
    result = dbCursor.execute('SELECT * FROM states')
    view = dbCursor.fetchall()
    myDb.close()
    for i in view:
        print(i)
