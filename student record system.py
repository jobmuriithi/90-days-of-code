students = [
    {"name": "John Doe", "age": 20, "major": "Computer Science", "Score": 85},
    {"name": "Jane Smith", "age": 22, "major": "Mathematics", "Score": 90},
    {"name": "Michael Johnson", "age": 21, "major": "Physics", "Score": 78},
    {"name": "Emily Davis", "age": 19, "major": "Biology", "Score": 92},
    {"name": "William Brown", "age": 23, "major": "Chemistry", "Score": 88},
]

def display_students(students):

    for student in students:

        print(
            f"{student['name']} |"
            f"{student['major']} |"
            f"{student['Score']} |"
        )

display_students(students)

