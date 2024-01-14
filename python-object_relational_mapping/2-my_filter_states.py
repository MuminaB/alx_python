""" 
    Script that takes in an argument and displays all values in the state
"""
import sys
import MySQLdb

db = MySQLdb.connect(name=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()
c.execute("SELECT * FROM states WHERE BINARY name = '{}'".format(sys.argv[4]))

states = c.fetchall()
for state in states:
    print(state)
     
