"""
    1. python -m ensurepip --upgrade OR python3 -m ensurepip --upgrade
    2. pip install emoji OR pip3 install emoji
"""

import sys
from emoji import emojize

# """ 
# text = input("Input: ")
# emojized = emojize(text, language='alias')
# """

emojized = emojize(sys.argv[1], language='alias') # this enables to input arguments with command-line in terminal

print(f"Output: {emojized}")