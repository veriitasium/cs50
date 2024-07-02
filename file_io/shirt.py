#under revision yet

from sys_arg_len import sys_arg_len
import sys
# pip3 install Pillow
from PIL import Image
from PIL import ImageOps
import os

sys_arg_len(3)

file_dir = os.path.dirname(__file__)

input, output = os.path.join(file_dir, sys.argv[1]), os.path.join(file_dir, sys.argv[2])

if not (input.endswith((".jpg", ".jpeg", ".png")) and output.endswith((".jpg", ".jpeg", ".png"))):
    sys.exit("Invalid input")


if os.path.splitext(input) == os.path.splitext(output):
    sys.exit("Input and output have different extensions")

size = (100, 150)

try:
    with Image.open(input) as shirt:
        size = shirt.size

        fit_shirt = ImageOps.fit(shirt, size)
        fit_shirt.paste(shirt, shirt)
        fit_shirt.save(output)

except FileNotFoundError:
    sys.exit("File is not found")