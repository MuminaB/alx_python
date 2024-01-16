"""
    Script that takes in the name of a state as an argument and lists all cities
    of that state.Script is injection free and takes in 4 arguments...
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states \
              ON cities.state_id = states.id WHERE states.name = '{}';" .format(sys.argv[4]))
    
    states = c.fetchall()
   
    print(", ".join([state[1] for state in states]))
            
