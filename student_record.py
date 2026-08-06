from student_record_system import delete_student


students = {}

#Adding students to the system.
def add_student():
    name = input("Enter student name: ").title()

    if name in students:
        print("Student already exists.")
        return

    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    students[name] = {
        "Age" : age,
        "Course" : course
    }
    print(f"{name} has been added to the system.")



#Search Student in the system.
def search_student():
    name = input("Enter student name to search: ").title()

    if name in students:
        print("\nStudent Found 👍👍")
        print("Name:", name)
        print("Age:", students[name]["Age"])
        print("Course:", students[name]["Course"])

    else:
        print("Student not found in the system.")


#Update the student
def update_student():
    name = input("Enter student name to update: ").title()

    if name in students:
        print("\nStudent Found 👍👍")
        print("Name:", name)
        print("Age:", students[name]["Age"])
        print("Course:", students[name]["Course"])

        age = int(input("Enter new age: "))
        course = input("Enter new course: ")

        students[name]["Age"] = age
        students[name]["Course"] = course

        print(f"{name}'s record has been updated.")

    else:
        print("Student not found in the system.")


    #Delete the student
    def delete_student():
        name = input("Enter student name to delete: ").title()

        if name in students:
            del students[name]
            print(f"{name} has been deleted from the system.")
        else:
            print("Student not found in the system.")


#Display all students in the system.
def display_students():
    if not students:
        print("No students in the system.")
        return

    print("\nStudent Records:")
    for name, details in students.items():
        print(f"Name: {name}, Age: {details['Age']}, Course: {details['Course']}")


#Main menu for the student record system.
while True:
    print("\nStudent Record System")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        display_students()
    elif choice == '6':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")



              



