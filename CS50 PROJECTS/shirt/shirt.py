import sys
from PIL import Image, ImageOps
import os

def main ():
    try:
        check_command_line()
        shirt = Image.open("shirt.png")
        image = Image.open(sys.argv[1])
        size = shirt.size
        image = ImageOps.fit(image, size)
        image.paste(shirt, shirt)
        image = image.save(sys.argv[2])
        
    except FileNotFoundError:
        sys.exit("Input does not exist")

def check_command_line():

    extension = [".jpg", ".jpeg", ".png"]
    root_ext1 = os.path.splitext(sys.argv[1])
    root_ext2 = os.path.splitext(sys.argv[2])

    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if root_ext1[1] not in extension or root_ext2[1] not in extension :
        sys.exit("Invalid output")
    if root_ext1[1] != root_ext2[1]:
        sys.exit ("Input and output have different extensions")
    if len(sys.argv)>3 :
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()