#Problem

#Understand the problem

#Break it down

#Look for a pattern

#Choose an approach or a strategy

#Write the code

#Test

#Improve



#Frequency counting pattern
scores = [70,80,70,90,80,70,60]

  #70: 3,
  #80: 2,
  #90: 1,
  #60: 1


scores = [70, 80, 70, 90, 80, 70, 60]

frequency = {}

for score in scores:
    if score in frequency:
        frequency[score] += 1
    else:
        frequency[score] = 1

print(frequency)


#TWO POINTERS
numbers = [1,2,3,4,5,6,7,8,9,10]

target = 10

left = 0
right = len(numbers) - 1

while left < right:

    total = numbers[left] + numbers[right]

    if total == target:
        print("Found:", numbers[left], numbers[right])

        break

    elif total < target:
        left += 1

    else:
        right -= 1


#PATTERN SEARCHING

def linear_search(items, target):

    for index in range(len(items)):
        if items[index] == target:
            return index

    return -1

students = ["Alice", "Bob", "Charlie", "David"]

result = linear_search(students, "JOB")

print(result)


#SORT THEN SEARCH
scores = [70, 80, 70, 90, 80, 70, 60]

scores.sort()
print(scores)

#