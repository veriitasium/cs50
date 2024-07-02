import csv
import os
import sys

from sys_arg_len import sys_arg_len 

sys_arg_len(3)

csv_path = sys.argv[1]

updated_csv = sys.argv[2]

script_dir = os.path.dirname(__file__)

students = []

try:
    with open(os.path.join(script_dir, csv_path)) as csv_file:
        reader = csv.DictReader(csv_file)
        
        for row in reader:
            first, last = [name.strip() for name in row["name"].split(",")]
            house = row["house"].strip()
            students.append({ "first": first, "last": last, "house": house })

except FileNotFoundError:
    sys.exit(f"Could not read {csv_path}")

# "a" -> adding | "w" -> writing (rewriting)
with open(os.path.join(script_dir, updated_csv), "w", newline="") as csvfile:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(csvfile, fieldnames)

    writer.writeheader()

    for student in students:
        writer.writerow(student)