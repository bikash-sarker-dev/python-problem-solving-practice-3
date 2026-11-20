# Task: Employee Salary Management System
import json

emp_name = input("Enter Name: ")
emp_id = input("Enter ID: ")
emp_salary = int(input("Enter Salary: "))

# create function 
def add_employee(name, id, salary):

    with open('employess.txt', 'a') as f:
        f.write(f"{name} | {id} | {salary}\n")

    return "The saves the data into the file."

        
  


def view_employees():
    try:
        with open('employess.txt', 'r') as f:
            emp_content = f.read()
            print(emp_content)

            print("Employee Added Successfully")

    except FileNotFoundError:
        print("No Employee Records Found!")



emp = add_employee(emp_name,emp_id,emp_salary)

print(emp)


view_employees()






    

