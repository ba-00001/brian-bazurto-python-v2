# Assignment 2 - Data Structures and File Handling
# Brian Bazurto
import csv
import os
import traceback
from datetime import datetime

import custom_module


def print_exception(e):
    # same error report as diary.py, then stop the program
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
    exit()


# Task 2: Read a CSV file
def read_employees():
    result = {}
    rows = []
    try:
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    result["fields"] = row
                else:
                    rows.append(row)
        result["rows"] = rows
        return result
    except Exception as e:
        print_exception(e)


employees = read_employees()
print(employees)


# Task 3: Find the column index
def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")


# Task 4: Find the employee first name
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]


# Task 5: Find the employee, a function in a function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6: Find the employee with a lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches


# Task 7: Sort the rows by last_name using a lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]


sort_by_last_name()
print(employees)


# Task 8: Create a dict for an employee
def employee_dict(row):
    result = {}
    for field, value in zip(employees["fields"], row):
        if field != "employee_id":
            result[field] = value
    return result


print(employee_dict(employees["rows"][0]))


# Task 9: A dict of dicts, for all employees
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        result[row[employee_id_column]] = employee_dict(row)
    return result


print(all_employees_dict())


# Task 10: Use the os module
def get_this_value():
    return os.getenv("THISVALUE")


# Task 11: Creating your own module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


set_that_secret("open sesame")
print(custom_module.secret)


# Task 12: Read minutes1.csv and minutes2.csv
def read_csv_as_tuples(path):
    # helper so both minutes files get read the same way (DRY)
    result = {}
    rows = []
    try:
        with open(path, "r", newline="") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    result["fields"] = row
                else:
                    rows.append(tuple(row))
        result["rows"] = rows
        return result
    except Exception as e:
        print_exception(e)


def read_minutes():
    minutes1 = read_csv_as_tuples("../csv/minutes1.csv")
    minutes2 = read_csv_as_tuples("../csv/minutes2.csv")
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)


# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)


minutes_set = create_minutes_set()


# Task 14: Convert to datetime
def create_minutes_list():
    minutes = list(minutes_set)
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes))


minutes_list = create_minutes_list()
print(minutes_list)


# Task 15: Write out sorted list
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        for row in converted:
            writer.writerow(row)
    return converted


write_sorted_list()
