#A program that gets or sends informaon to another application through an API

#The Basic API project structure

            #Get Input

            #Build request

            #Send request

            #Receive response

            #Check status

            #Convert to JSON

            #Extract information

            #Display information/ Use information

import requests

response = requests.get(url)

if response.ok:
    data = response.json()
    # Use the data

    