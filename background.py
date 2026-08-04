from rembg import remove
from PIL import Image

input = Image.open("JOBS.jpg.png")

output = remove(input)

output.save("output.png")

