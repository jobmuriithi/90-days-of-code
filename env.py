import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
student_name = os.getenv("STUDENT_NAME")

print(app_name)
print(student_name)

