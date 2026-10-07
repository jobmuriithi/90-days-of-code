import requests

url = "https://randomuser.me/api/"

response = requests.get(url)

if response.ok:
    data = response.json()

    user = data["results"][0]

    first_name = user["name"]["first"]

    last_name = user["name"]["last"]

    email = user["email"]

    country = user["location"]["country"]


    print("============================")

    print("          RANDOM USER")
    print("============================")

    print(f"Name: {first_name} {last_name}")
    print(f"Email: {email}")
    print(f"Country: {country}")
else:
    print("Failed to retrieve data from the API.")