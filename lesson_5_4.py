import sqlite3

"""Connecting to an existing database"""



"""New database creation"""
db = sqlite3.connect('test_sql.db')  # database creation
print("Connected to the database")
cur = db.cursor()  # Variable to control the database



"""Table creation"""
cur.executescript("""CREATE TABLE IF NOT EXISTS Students2(
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
	First_name TEXT NOT NULL,
	Last_name TEXT NOT NULL);
	INSERT INTO Students2(First_name, Last_name)
    VALUES('Petr', 'Petrov');
""")
db.commit()  # Saving a request
print("Students table created")

