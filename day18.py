#MODULES, PACKAGES & FILE HANDLING
#MODULES(a file)
#A python file that contains code which can be used in any program

#importing modules

#PACKAGES(a folder)
#A folder that contains multiple related modules


#FILE HANDLING
#Opening a file
#Format open(filename, mode)

#Read a file
file = open("gettersandsetters.py","r")
print(file.read())
file.close()


#Reading line by line
file = open("grade_calculator.py","r")

for line in file:
    print(line)

file.close()

#Writting a file
file = open("LIBRARY_COLLECTION.PY","w")

file.write("NAIROBI\n")
file.write("KENYA\n")

file.close()


#Appending to a file
file = open("LIBRARY_COLLECTION.PY","a")
file.write("MOI AVENUE\n")
file.close()

#using with
with open("LIBRARY_COLLECTION.PY","r") as file:
    print(file.read())
    