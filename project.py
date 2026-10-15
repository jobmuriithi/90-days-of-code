import sqlite3

DATABASE_NAME = 'students.db'

def connect_database():
    """Connect to the database and enable foreign key."""
    connection = sqlite3.connect(DATABASE_NAME)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def create_tables():
    """Create the students table if it does not exist."""

    with connect_database() as connection:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                student_name TEXT NOT NULL
                course TEXT NOT NULL
                year INTEGER NOT NULL CHECK (between 1 AND 8)
            )
        ''')

        print("Database is ready.")

def add_student():
    """Add a new student to the database."""
    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()
    year_text = input("Enter year (1-8): ").strip()

    if not name or not course or not year_text:
        print("All fields are required.")
        return
    
    try:
        year = int(year_text)
        if not 1 <= year <= 8:
            print("Year must be between 1 and 8.")
            return

            with connect_database() as connection:
                connection.execute('''
                    INSERT INTO students (student_name, course, year)
                    VALUES (?, ?, ?)
                ''', (name, course, year))
                print("Student added successfully.")

    except ValueError:
        print("Year must be a valid integer.")

        except sqlite3.IntegrityError:
            print("Error: Could not add student. Please check the data and try again.")

