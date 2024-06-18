# pip3 install pyfiglet

import sys
from pyfiglet import Figlet

figlet = Figlet()

try:
    font, name = sys.argv[1], sys.argv[2]
    
    if (font != '-f' and font != '--font') or name not in figlet.getFonts():
        sys.exit("Invalid usage")
except IndexError:
    sys.exit("Invalid usage")

text = input("Input: ")

figlet.setFont(font=name)
print(figlet.renderText(text))