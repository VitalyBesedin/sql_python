import sqlite3

"""Connecting to an existing database"""

# db = sqlite3.connect(r'/Users/vitalybesedin/Documents/SQLite/qa_testing.db')  # database connection
# print("Connected to the database")
# cur = db.cursor()  # Variable to control the database
# cur.execute("""SELECT * FROM Students;""")  # Query to get the contents of the Students table
# result = cur.fetchall()  # Request result
# print(result)
# print(type(result))

db = sqlite3.connect('test_sql.db')  # database creation
print("Connected to the database")
cur = db.cursor()  # Variable to control the database