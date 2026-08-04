def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

print("Addition: 5 + 3 =", add(5, 3))
print("Subtraction: 10 - 4 =", subtract(10, 4))
print("Multiplication: 6 * 7 =", multiply(6, 7))
print("Division: 15 / 3 =", divide(15, 3))

