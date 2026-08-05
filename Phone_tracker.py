import phonenumbers
from phonenumbers import geocoder


phone_number1 = phonenumbers.parse("+245798026361")
phone_number2 = phonenumbers.parse("+245729757595")
phone_number3 = phonenumbers.parse("+245715052924")


print("\nPhone Number Location\n")

print("Phone Number 1:", geocoder.description_for_number(phone_number1, "en"))
print("Phone Number 2:", geocoder.description_for_number(phone_number2, "en"))
print("Phone Number 3:", geocoder.description_for_number(phone_number3, "en"))

#Let's crack it
#Follow for more coding tutorials and projects
#It's JOBS Baby😊😊❤️❤️❤️
