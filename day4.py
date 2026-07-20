first_name = "JOB"
last_name = "MURIITHI"
age = 20
weight = 70.5
course = "Computer Science"
Has_a_laptop = True
python_experience = "Beginner"

def myfunc():
    global python_experience
    python_experience = "Intermediate"

myfunc()

print ("FIRST NAME:", first_name)
print ("LAST NAME:", last_name)
print ("AGE:", age)
print ("WEIGHT:", weight)
print ("COURSE:", course)
print ("HAS A LAPTOP:", Has_a_laptop)
print ("PYTHON EXPERIENCE:", python_experience)
