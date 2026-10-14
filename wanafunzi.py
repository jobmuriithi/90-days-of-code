import sqlite3

#connects to the database
connection = sqlite3.connect("wanafunzi.db")
print("Connection successfull!!")

cursor = connection.cursor()
#The cursor allows python to execute SQL statements and retrieve their results

cursor.execute("""CREATE TABLE IF NOT EXISTS students

(students_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
course TEXT NOT NULL,
year INTEGER NOT NULL)
""")

connection.commit()

connection.close()

print("Students table has been created")

#CRUD Operations
#C Create
#R Read
#U Update
#D Delete

cursor.execute("""
INSERT INTO wanafunz.db (name,course,year) VALUES(?,?,?)""", ('Alice','Computer Science',2))

connection.commit()

