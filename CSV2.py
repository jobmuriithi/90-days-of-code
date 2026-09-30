import csv

with open("students.csv","r") as file:

    reader = csv.DictReader(file)

    for student in reader:

        print(student["name"])
        print(student["course"])
        print(student["score"])

