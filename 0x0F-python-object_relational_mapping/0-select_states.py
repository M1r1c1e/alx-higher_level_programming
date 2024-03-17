#!/usr/bin/python3
""" listing all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    dbCon = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3])
    cursor = dbCon.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    dbCon.close()
    
