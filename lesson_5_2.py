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

# """Table creation"""
# cur.execute("""CREATE TABLE IF NOT EXISTS Students(
#     StudentID INTEGER PRIMARY KEY,
# 	First_name TEXT NOT NULL,
# 	Last_name TEXT NOT NULL
# );""")
# db.commit()  # Saving a request
# print("Studets table created")
#
# """Filling in the table Students"""
# cur.execute("""INSERT INTO Students(First_name, Last_name)
#     VALUES('Petr', 'Petrov');""")
# db.commit()  # Saving a request

"""Table creation"""
cur.execute("""CREATE TABLE IF NOT EXISTS Students1(
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
	First_name TEXT NOT NULL,
	Last_name TEXT NOT NULL
);""")
db.commit()  # Saving a request
print("Studets table created")

# """No secure - way Filling in the table Students"""
# cur.execute("""INSERT INTO Students1(First_name, Last_name)
#     VALUES('Petr', 'Petrov');""")
# db.commit()  # Saving a request


"""Secure way - Filling in the table Students"""
data_students = ('Semen', 'Semenov')
cur.execute("""INSERT INTO Students1(First_name, Last_name)
    VALUES(?, ?);""", data_students)
db.commit()  # Saving a request