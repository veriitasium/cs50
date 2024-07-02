# pip3 install tabulate

import os
from tabulate import tabulate
import sys
import csv

from sys_arg_len import sys_arg_len

sys_arg_len(2)

path = sys.argv[1]

if ".csv" not in path:
    sys.exit("Not a CSV file")

script_dir = os.path.dirname(__file__)

try:
    with open(os.path.join(script_dir, path)) as csvfile:
        reader = csv.reader(csvfile)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))
        
except FileNotFoundError:
    sys.exit("File is not found")