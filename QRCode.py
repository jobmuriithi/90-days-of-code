#DAY 8 OF LEARNING PYTHON WITH JOB

#TODAY WE ARE CREATING A QR CODE GENERATOR

import qrcode

data = input("Enter your link: ")

img = qrcode.make(data)

img.save("qr.png")

img.show()

print("YOUR QR CODE HAS BEEN GENERATED SUCCESSFULLY!!!")

print("DON'T FORGET TO FOLLOW, LIKE, SHARE & COMMENT ")

#SEE YOU IN DAY 9