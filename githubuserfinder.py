import requests

username = input("Enter your GitHub username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Username:",data["login"])
    print("Name:", data["name"])
    print("Followers:", data["followers"])
    print("Following:", data["following"])
    print("Repositories:", data["public_repos"])

elif response.status_code == 404:
    print("User not found.")
else:
    print("Something went wrong>>>>")

