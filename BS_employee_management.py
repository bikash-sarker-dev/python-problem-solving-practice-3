# Task: Employee Salary Management System


employee_list = []
# create function 
def add_employee(name, id, salary):

    create_employee = {
        "name": name,
        "id": id,
        "salary": salary,
    }

    employee_list.append(create_employee)

    return employee_list



add_employee("jamal",'343','30000')
add_employee("jamal2",'34354','300004')
add_employee("jamal3",'34354','300004')

print(employee_list)