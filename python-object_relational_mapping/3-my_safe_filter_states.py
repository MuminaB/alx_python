"""
    Script that is safe from MySQL Injection...
    Takes four arguments
"""
import sys
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")

    states =c.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
             
