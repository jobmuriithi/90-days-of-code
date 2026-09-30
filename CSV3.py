import csv

students = [
    ["Joel", "Software Engineering", 96],
    ["Job", "Data Science", 97],
    ["caleb", "Software Engineering", 89]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "course", "score"])

    for student in students:
        writer.writerow(student)