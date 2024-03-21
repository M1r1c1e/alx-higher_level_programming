#!/usr/bin/python3
""" taking in the name of a state as an argument
    and listing all `cities` of that state, using the database `hbtn_0e_4_usa`
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT c.id, c.name, s.name FROM cities as c\
                    inner join city as s\
                    ON c.state_id = s.id\
                    WHERE s.name = %s", (sys.argv[4],))
    cities = cursor.fetchall()

    print(", ".join([city[1] for city in cities]))

    cursor.close()
    db.close()
