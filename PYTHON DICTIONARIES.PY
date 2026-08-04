
# Accessing values in a dictionary using functions

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

# Store function results in a dictionary
message = {
    "hello": greet("John"),
    "goodbye": farewell("Alice")
}

# Access dictionary values
print(message["hello"])
print(message["goodbye"])


