"""
Script that lists all cities from a database
"""
import sys
import MySQLdb

db = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])
c = db.cursor()
c.execute("SELECT cities.id, cities.name, states.name FROM cities\
          JOIN states ON cities.state_id = states.id;")

states = c.fetchall()
for state in states:
    print(state)
     
