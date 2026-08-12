#SETS
#A set is acollection of unique elements

fruits = {"Banana","Mango"}
print(fruits)


#Creating sets
numbers = {1,2,3,4,5,6}
print(numbers)

numbers = set([9,8,7,0])
print(numbers)

names = [
    "JOB",
    "JOB",
    "Joel",
    "Mark",
    "Lucy",
    "lucy"
    ]

first_names = set(names)
print(first_names)

#Mistakes to avoid
my_set = {}
print(type(my_set))

my_set = set()
print(type(my_set))

numbers = {1,1,1,1,2,2,2,3,3,3,9,9,9,}
print(numbers)

names = {
    "Betsy",
    "Kimani",
    "Jolee",
    "Kimani"
}

print(names)

number = {10,20,30,40,50}
print(number) #sets are unordered


#Adding
student = {"Joshua","Kering","Stacy"}
student.add("Peter")
print(student)

student.update(["David","Alice"])
print(student)

student.remove("Stacy")
print(student)

student.discard("Jane")
print(student)

students = student.pop()
print(students)

cars = {"Toyota","honda"}
cars.clear()
print(cars)


#Membership testing
Animals = {"Man","lion","giraffe"}
print("Elephant" in Animals)
for animal in Animals:
    print(animal)

python_students = {"Mary","Ferguson","charlie","Ben"}
java_students = {"Mary","Ferguson","Ned","Prian"}

all_students = python_students|(java_students)
print(all_students)   

common_students = python_students & (java_students)
print(common_students)

only_python = python_students - (java_students)
print(only_python)

result = python_students^(java_students)
print(result)

