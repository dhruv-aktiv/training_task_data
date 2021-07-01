
# CLASS WITH CONSTRUCTORS


class Employee:
    emp_name = ''
    emp_desig = ''
    emp_salary = int(0)

    def __init__(self, emp_name, emp_desig='Python/Odoo Developer', emp_salary=25000):
        self.emp_name = emp_name
        self.emp_desig = emp_desig
        self.emp_salary = emp_salary


if __name__ == '__main__':
    input_emp_name, input_emp_desig, input_emp_salary = input(
        "Enter emp_name, emp_desgination, emp_salary : ").split(',')
    input_emp_name = input_emp_name
    input_emp_desig = input_emp_desig
    input_emp_salary = input_emp_salary
    employee = Employee(input_emp_name, input_emp_desig, input_emp_salary)
    print(f"employee name : {employee.emp_name}")
    print(f"employee designation : {employee.emp_desig}")
    print(f"employee salary : {employee.emp_salary}")
