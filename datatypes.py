#Data Types
# INTEGER Stores whole numbers
# STRING  Stores text
# FLOAT  Stores decimal numbers
# BOOLEAN  Stores True or False values

#Type 
year = "2015"
university = "Jomo Kenyatta University of Agriculture and Technology"
year = 1998

print (year)

#GLOBAL VARIABLES
X = "NAIROBI"

def myfunc():
    global X
    X = "MOMBASA"

myfunc()
print ("I live in", X)







