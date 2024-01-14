"""
    Script that lists all states from a selected database
    Takes three arguments: username, password and database name
"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])
    cursor = database.cursor()
    rows = cursor.execute("SELECT * FROM `states`")
    #[print(state) for state in cursor.fetchall()]
    results = cursor.fetchall
    for result in results:
        print(result)
    # db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # cursor = db.cursor()
    # cursor.execute("SELECT * FROM `states`")
    # [print(state) for state in cursor.fetchall()]
      
