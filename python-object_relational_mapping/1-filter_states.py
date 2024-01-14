"""
    Script that lists all states with name starting with N from a selected database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")

    states = cursor.fetchall()
    for state in states:
        if state[1][0] == "N":
            print(state)
              
