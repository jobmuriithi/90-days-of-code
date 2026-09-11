#LISTS COMPREHENSIONS, DICTIONARIES, SETS + DATA STRUCTURES PROJECTS

numbers = [10,15,20,25,30]

result = []

for number in numbers:
    if number > 20:
        result.append(number)

print(result)

students = ["John", "Mary", "Brian", "Jane"]

print(students[0])
print(students[-1])

students.append("Mike")
print(students)

students.sort()
print(students)

marks = [65,78,45,90,56,82]
print(max(marks))
print(min(marks))
print(sum(marks))

average = sum(marks)/len(marks)
print(average)

#LISTS COMPREHENSIONS

numbers = [1,2,3,4,5]

squares = []

for number in numbers:
    squares.append(number**2)

print(squares)

numbers = [1,2,3,4,5]

squares = [number**2 for number in numbers]
print(squares)

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers) 

marks = [45,67,89,32,76,90]
passed = [mark for mark in marks if mark >= 50]

print(passed)


#DICTIONARIES COMPREHENSIONS
#General structure
#{key: value for item in iterable}

students = ["John", "Mary", "Brian", "Jane"]

students_ids = {
    name: index + 1 for index, name in enumerate(students)
}

print(students_ids)

#DATA STRUCTURES MINI PROJECT
#STUDENT PERFORMANCE ANALYZER

students = [
    {"name": "John", "marks": 78},
    {"name": "Mary", "marks": 92},
    {"name": "Brian", "marks": 45},
    {"name": "Jane", "marks": 67},
    {"name": "Mike", "marks": 88}
]
for student in students:
    print(student["name"])

marks = [student["marks"] for student in students]

print(marks)

passed = [
    student["name"]
    for student in students if student["marks"] >= 50
]
print(passed)

student_marks = {
    student["name"]: student["marks"] for student in students
}
print(student_marks)
