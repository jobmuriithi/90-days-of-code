# Student Record System

students = {}

def add_student():
    name = input("Enter student name: ")

    if name in students:
        print("Student already exists.")
        return

    age = int(input("Enter age: "))
    course = input("Enter course: ")

    students[name] = {
        "Age": age,
        "Course": course
    }

    print("Student added successfully.")


def search_student():
    name = input("Enter student name: ")

    if name in students:
        print(students[name])
    else:
        print("Student not found.")


def update_student():
    name = input("Enter student name: ")

    if name in students:
        age = int(input("Enter new age: "))
        course = input("Enter new course: ")

        students[name]["Age"] = age
        students[name]["Course"] = course

        print("Updated successfully.")
    else:
        print("Student not found.")


def delete_student():
    name = input("Enter student name: ")

    if name in students:
        del students[name]
        print("Deleted successfully.")
    else:
        print("Student not found.")


def display_students():
    if not students:
        print("No students available.")
    else:
        for name, info in students.items():
            print("----------------------")
            print("Name:", name)
            print("Age:", info["Age"])
            print("Course:", info["Course"])


while True:

    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        display_students()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")