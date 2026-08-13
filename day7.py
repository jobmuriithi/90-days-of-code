#DAY 7

#LOOPS
#Repeat something

print ("Today is on Thursday")
#We want to print this 100 times

#TYPES OF LOOPS
#while loops
#for loops

#WHILE LOOPS

#while condition:
    #code

cake = 1

while cake <= 9:
    print(cake)
    cake += 2


#infite loop
#cake = 1
#while  cake <= 9:
    #print(cake)


#FOR LOOPS
#Repeat over a sequence


for numbers in range(7):
    print(numbers)

#RANGE
#range(5) prints 0 - 4

for i in range(5):
    print(i)

for i in range(0,12,4):
    print(i)

for i in range(1,6):
    print(i)

#LOOPING THROUGH STRINGS
for  letters in "PYTHON":
    print(letters)

#BREAK
#stops the loop immediately

for i in range (1,11):
    if i==6:
        break
    print(i)

#continue
#skips one iteration

for i in range(1,11):
    if i == 5:
        continue
    print(i)


#PASSWORD CHECKER
password = ""
while password != "12345":
    password = input("Enter your password: ")

print("WELCOME")