"""
    Script that lists all states from a selected database
    Takes three arguments: username, password and database name
"""
import MySQLdb
if __name__ == "__main__":
    database = MySQLdb.connect(user = "mumi", passwd = "password", db = "hbtn_0e_0_usa")
    cursor = database.cursor()
    cursor.execute("SELECT * FROM `states`")
    #[print(state) for state in cursor.fetchall()]
    results = cursor.fetchall
    for result in results:
        print(result)
     
