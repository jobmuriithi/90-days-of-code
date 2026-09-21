def hello():
    print("hello")
    hello()

#Every recursive function needs a condition that tells it when to stop.
#The condition is called the base case.

def countdown(n):

    if n == 0:
        print("happy new year!")
        return

    print(n)

    countdown(n - 1)

countdown(5)

#CALL STACK 

#Factorial
#5! = 5 * 4 * 3 * 2 * 1 = 120


def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

#factorial(5) = 5 * factorial(4)
#factorial(4) = 4 * factorial(3)
#factorial(3) = 3 * factorial(2)
#factorial(2) = 2 * factorial(1)
#factorial(1) = 1

#2 * 1 = 2
#3 * 2 = 6
#4 * 6 = 24
#5 * 24 = 120

def factorial_loop(n):

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial_loop(5))

