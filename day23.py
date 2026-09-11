#SEARCHING AND SORTING

#Searching
#Finding a particular item in a collection.

#Sorting 
#Arranging items into a particular order

#SEARCHING
#Linear searching

students =  ["John","Mary","Joseph","Tatiana","Jane"]
target = "Jane"

for student in students:
    if student == target:
        print(f"{target} found....")
        break

students = ["John","Mary","Joseph","Tatiana","Jane"]
target = "Jane"

for i in range(len(students)):
    if students[i] == target:
        print(f"{target} found at index {i}....")
        break


#BINARY SEARCH

numbers = [10,20,30,40,50,60,70,80,90]
target = 70

low = 0
high = len(numbers) - 1

while low <= high:

    middle = (low + high) // 2

    if numbers[middle] == target:
        print(f"{target} found at index {middle}....")
        break

    elif numbers[middle] < target:
        low = middle + 1

    else:
        high = middle -1


#SORTING
numbers = [5,2,9,1,7]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print(sorted(numbers, reverse=True))

#SORTED vs SORT
#sorted()
#Returns a new list

numbers = [5,2,9,1]
new_numbers = sorted(numbers)

print(numbers)
print(new_numbers)

#sort()
#Changes the original list

numbers = [5,2,9,1]
numbers.sort()
print(numbers)

