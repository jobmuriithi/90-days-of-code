#INPUT , OUTPUT & TYPE CONVERSION

#OUTPUT
print("Hello, World!")
print("Today is day 5 of learning python")

#USER INPUT
name = input("Enter your name: ")
print ("What's up " + name)

#F STRINGS
#Easier to read
#No need to convert data types manually
#You can include operators + - * / 

age = input("When were you born? ")
print (f"You are {2026 - int(age)} years old")

height = input("What is your height in meters? ")


#ERRORS
age = int(input("When were you born? "))

print (age +10)

#TYPE CONVERSION
#This is changing the value from one data type to another

age = 20
print (float(age))

#STRINGS AND INDEXING

county = "Nairobi"

print (county[0])
print (county[1])
print (county[-1])
print (county[:4])

name = "Job Muriithi"
print (name.upper())
print (name.lower())
print (name.split())
print (name.replace("Job", "JOBS"))
print (name.strip())

#joIN 
#JOINS A LIST INTO ONE STRING




