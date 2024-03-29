import sqlite3

"""Connecting to an existing database"""

db = sqlite3.connect('test_sql.db')  # database creation
print("Connected to the database")
cur = db.cursor()  # Variable to control the database


"""Table data update"""
update_params = ('Sokolova', 4)
cur.execute("""UPDATE Students1 SET Last_name = ? WHERE StudentID = ?;""", update_params)
# cur.execute("""UPDATE Students1 SET Last_name = 'Orlova' WHERE StudentID = 4""")
db.commit()  # Saving a request
print("Students1 table updated")

