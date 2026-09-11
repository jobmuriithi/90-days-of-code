#CODING FRIDAY


cars = ["BMW", "Volvo", "Ford","Mazda", "Toyota", "Honda", "Nissan", "Chevrolet", "Kia", "Hyundai"]
target = "Toyota"

for car in cars:
    if car == target:

        print(f"{target} found....")
        break


def linear_search(items, target):

    for item in items:
        if item == target:
            return True

    return False

students = ["Brian","Job","Mercy","Joel","Paul","Freshier"]
result = linear_search(students,"Briana")

print(result)

#BUBBLE SORTING
numbers = [5,3,8,4,2]

n = len(numbers)

for i in range(n):

    for j in range(0, n - i - 1):

        if numbers[j] > numbers[j + 1]:

            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


print(numbers)

