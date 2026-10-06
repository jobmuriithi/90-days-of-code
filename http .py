#HTTP - HyperText Transfer Protocol

#Is a set of rules which allow computers to communicate over the internet. 

#https://jobsy.co.ke

#https://google.com


#HTTP request and response

#Request - Is what your computer asks the server for.

#Response - What the server sends back.

#Browser - Request - Server
#Browser - Response - Server

#Server - Is a computer that provides something to other computers.

#API - Application Programming Interface 

#https://example.com/api/jobs

#[
 #   {
 #       "title": "Python Developer",
  #      "Company": "Safricom PLC"
   # },
    #{
     #   "title": "Data Analyst,
      #  "Company": "IBM"
    #}
#]


#HTTP Methods

#GET - Get Information
#POST - Send/Create information
#PUT - Update information
#PATCH - Partially update information
#DELETE - Delete information

#GET Request
#GET /users

#POST Request
#POST /users
#{
  #  "name": "Alice",
 #   "email": "alice@example.com"
#}

#HTTP status codes
#200 - OK
#201 - Created
#400 - Bad Request
#403 - You don't have permission
#404 - Not Found
#500 - Internal Server Error

#How to make a http request in python


import requests
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

data = response.json()

print(data)

