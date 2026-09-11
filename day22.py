#START

#Ask the user for the first number
#Ask the user for the second number

#IF first number is greater than second number
        #Display first number
#ELSE
        #Display Second number


#END


num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is larger.")
else:
    print(f"{num2} is larger.")


