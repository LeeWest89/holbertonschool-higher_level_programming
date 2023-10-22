#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
    cursor.close()
    db.close()
