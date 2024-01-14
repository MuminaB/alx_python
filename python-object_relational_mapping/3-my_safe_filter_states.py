"""
    Script that is safe from MySQL Injection...
    Takes four arguments
"""
import sys
import MySQLdb
db = MySQLdb.connect(name=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()
c.execute("")
