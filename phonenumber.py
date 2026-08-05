import phonenumbers
from phonenumbers import carrier, timezone

number = phonenumbers.parse("+254798026361")

print("Carrier/ Service Provider: ", carrier.name_for_number(number, "en"))
print("Time Zone: ", timezone.time_zones_for_number(number))

#Happy coding❤️❤️
#It's JOB Baby
