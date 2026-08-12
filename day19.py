#LISTS AND TUPLES
#Lists
# We are storing multiple variables in a single variable

student1 = "Mary"
student2 = "Ken"
student3 = "Hellen"
student4 = "Ben"

students = ["Mary","Ken","Hellen","Ben"]
numbers = [1,2,3,4,5,6.7,5.9]
mixed = ["John",29,True,3.142]

#List Indexing
fruits = ["Mango","Apple","Avocado","Pineapple"]

print(fruits[0])
print(fruits[-1])

#Changing the list elements
fruits[1] = "Dates"

print(fruits)

#Adding elements to a list
#append ---- Adds an element at the end

workers = ["Caroline","Matthew"]
workers.append("Peter")
print(workers)


#insert---- Adds an element at a specific position
workers.insert(1, "JOB")
print(workers)



#extend -- Adds multiple elements to the list
workers.extend(["Ruth","Joel"])
print(workers)


#Removing elements
#remove --- Removes a specific value
cars = ["Honda","Benz","Toyota","BMW"]
cars.remove("Honda")
print(cars)

#pop --- Removes an element using it's index
cities = ["Nairobi","Mombasa","Eldoret","Kisumu"]
cities.pop(1)
print(cities)


#del
towns = ["Machakos","Eastleigh","Mirema"]
del towns[1]
print(towns)

#clear
presidents = ["Jomo","Moi","Kibaki","Uhuru","Ruto"]
presidents.clear()
print(presidents)

#List slicing
numberz = [10,20,30,40,50,60]
print(numberz[1:4])
print(numberz[:3])
print(numberz[2:])

#Finding the length of a list
#len()
days = ["Monday","Tuesday","Wednesday","Thursday"]
print(len(days))



#Checking if an element exists
print("Friday" in days)
print("Monday" in days)

#Looping throuhg elements

for day in days:
    print(days)

#Nested lists
studentz = [
    ["John",20],
    ["Mary",80]
]

print(studentz[0])

people = ["mary","John"]
for person in people:
    print(people)
    