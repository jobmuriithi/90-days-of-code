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

print("Students table has been created")

#CRUD Operations
#C Create
#R Read
#U Update
#D Delete

cursor.execute("""
INSERT INTO students (name,course,year) VALUES(?,?,?)""", ('Alice','Computer Science',2))

connection.commit()


# Check whether the table exists
cursor.execute("""
SELECT name FROM sqlite_master
WHERE type = 'table' AND name = 'students'
""")

result = cursor.fetchone()

if result:
    print("The wanafunzi table exists!")
else:
    print("The table does not exist!")

connection.close()
