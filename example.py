import requests

response = requests.get("https://jsoplaceholder.typicode.com/users/1")

data = response.json()
print(data)