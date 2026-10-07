import requests

url = "https://randomuser.me/api/"

response = requests.get(url)

data = response.json()

data["results"][0]["name"]["first"]
