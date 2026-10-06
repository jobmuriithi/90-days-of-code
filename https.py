import requests

url = "https://jobsy.co.ke"

response = requests.get(url)

if response.status_code == 404:
    data = response.json()

    print("Company:",data["company"])

elif response.status_code == 404:
    print("User not found")

else:
    print("Error")
