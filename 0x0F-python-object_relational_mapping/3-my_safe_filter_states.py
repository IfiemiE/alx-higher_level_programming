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
    ns = sys.argv[4]
    if ns[0] == '"':
        ns = ns[1:]
    if ns[-1] == '"':
        ns = ns[:-1]
    for p in range(len(ns)):
        if (ns[p] == ';'):
            ns = ns[:(p - 1)]
            break
    myDb = MySQLdb.connect(host = 'localhost',
                            user = usr,
                            password = psswd,
                            db = dbase,
                            port = 3306)

    dbCursor = myDb.cursor()
    query = "SELECT * FROM states WHERE name = '{}'".format(ns)
    result = dbCursor.execute(query)
    view = dbCursor.fetchall()
    myDb.close()
    for i in view:
        print(i)
