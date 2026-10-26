# Task 3: List Comprehensions Practice
import csv

# read the whole csv into a list of lists
with open("../csv/employees.csv", "r", newline="") as file:
    rows = list(csv.reader(file))

# first_name is column 1 and last_name is column 2, rows[1:] skips the header
names = [row[1] + " " + row[2] for row in rows[1:]]
print(names)

# only keep the names that have a lowercase "e" in them
names_with_e = [name for name in names if "e" in name]
print(names_with_e)
