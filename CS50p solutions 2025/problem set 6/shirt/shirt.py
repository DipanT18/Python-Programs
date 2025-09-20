import sys
from PIL import Image, ImageOps

if (len(sys.argv) < 3):
    sys.exit("Too few command-line arguments")
if (len(sys.argv) > 3):
    sys.exit("Too many command-line arguments")
if sys.argv[1].split(".")[-1] not in ["png", "jpg", "jpeg"]:
    sys.exit("Invalid input")
if sys.argv[2].split(".")[-1] not in ["png", "jpg", "jpeg"]:
    sys.exit("Invalid output")
if sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
    sys.exit("Input and output have different extensions")

try:
    with Image.open("shirt.png") as shirt:
        with Image.open(sys.argv[1]) as subject:
            shirtSize = shirt.size
            resizedSubject = ImageOps.fit(subject, shirtSize)
            resizedSubject.paste(shirt,(0,0), shirt)
            resizedSubject.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
