#JSON 
#JavaScript Object Notation 

{
    "name": "John",
    "age": 30,
    "city": "New York"
}


#Converting a dictionary to JSON
import json
student = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}

data = json.dumps(student)
print(data)

import json
data = '{"name": "Alice", "age": 25, "city": "Los Angeles"}'
#Converting JSON to a dictionary
student = json.loads(data)
print(data)

