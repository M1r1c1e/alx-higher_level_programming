#!/usr/bin/python3
""" listing all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%';")
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
