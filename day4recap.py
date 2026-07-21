# DATA TYPES
#STRING Hello, World!
#INTEGER 2,29
#FLOAT 2.4
#BOOLEAN True False

#TYPE FUNCTION

day = "Monday"
time = 4
height = 5.9
python_level = "Beginner"

print (python_level)
print (type(python_level))

#GLOBAL VARIABLES

x = 10

def myfunc():
    global x
    x = 5
    print(x)
#A variable that is inside a function is considered temporary unless it is a global variable
myfunc()

print(x)

#PERSONAL PROFILE
first_name = "JOB"
last_name = "MURIITHI"
age = 20
height = 5.9
weight = 60
course = "Computer Science"
python_level = "Beginner"

def myfunc():
    global first_name
    first_name = "JOBS"
    print(first_name)

myfunc()

print(first_name)
print(last_name)
print(age)
print(height)
print(weight)
print(course)
print(python_level)