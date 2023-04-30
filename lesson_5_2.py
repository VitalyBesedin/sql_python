import sqlite3

"""Connecting to an existing database"""

# db = sqlite3.connect(r'/Users/vitalybesedin/Documents/SQLite/qa_testing.db')  # database connection
# print("Connected to the database")
# cur = db.cursor()  # Variable to control the database
# cur.execute("""SELECT * FROM Students;""")  # Query to get the contents of the Students table
# result = cur.fetchall()  # Request result
# print(result)
# print(type(result))

"""New database creation"""
db = sqlite3.connect('test_sql.db')  # database creation
print("Connected to the database")
cur = db.cursor()  # Variable to control the database

"""Table creation"""
cur.execute("""CREATE TABLE IF NOT EXISTS Students(
    StudentID INTEGER PRIMARY KEY,
	First_name TEXT NOT NULL,
	Last_name TEXT NOT NULL
);""")
db.commit()  # Saving a request
print("Studets table created")

"""Filling in the table Students"""
cur.execute("""INSERT INTO Students(StudentID, First_name, Last_name)
    VALUES(1, 'Ivan', 'Ivanov');""")
db.commit()  # Saving a request
