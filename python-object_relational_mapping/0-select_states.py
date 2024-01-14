"""
    Script that lists all states from a selected database
    Takes three arguments: username, password and database name
"""
import MySQLdb
database = MySQLdb.connect(user = "root", passwd = "password123", db = "hbtn_0d_0_usa")
cursor = database.cursor()
cursor.execute("SELECT * FROM `states`")
#[print(state) for state in cursor.fetchall()]
results = cursor.fetchall
for result in results:
    print(result)
     
