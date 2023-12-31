class SortableDictionaryList:
    def __init__(self):
        self._data = []

    def append(self, item):
        self._data.append(item)

    def sort(self, key="name", reverse=False):
        self._data.sort(key=lambda x: getattr(x, key), reverse=reverse)

    def __len__(self):
        return len(self._data)
    
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    department: str
    salary: float

def add_employee(employees):
    name = input("Enter the employee's name: ")
    age = int(input("Enter the employee's age: "))
    department = input("Enter the employee's department: ")
    salary = float(input("Enter the employee's salary: "))

    employee = Employee(name=name, age=age, department=department, salary=salary)
    employees.append(employee)
    print("Employee added successfully!")

def display_employees(employees: SortableDictionaryList):
    if employees.__len__() == 0:
        print("No employees in the system.")
    else:
        print("Employee details:")
        for employee in employees._data:
            print(f" - Name: {employee.name}, Age: {employee.age}, Department: {employee.department}, Salary: {employee.salary}")

def update_employee(employees: SortableDictionaryList):
    name = input("Enter the name of the employee to update: ")
    found_employee: None or Employee = None

    for employee in employees._data:
        if employee.name == name:
            found_employee = employee
            break

    if found_employee:
        new_salary = input("Enter the new salary: (Enter to skip): ")
        new_age = input("Enter the new age: (Enter to skip): ")
        new_department = input("Enter the new department: (Enter to skip): ")

        found_employee.salary = float(new_salary) if bool(new_salary) else found_employee.salary
        found_employee.age =  int(new_age) if bool(new_age) else found_employee.age
        found_employee.department = new_department if bool(new_department) else found_employee.department
        print("Employee details updated successfully!")
    else:
        print("Employee not found.")

def remove_employee(employees: SortableDictionaryList):
    name = input("Enter the name of the employee to remove: ")
    found_employee = None

    for employee in employees._data:
        if employee.name == name:
            found_employee = employee
            break

    if found_employee:
        employees._data.remove(found_employee)
        print("Employee removed successfully!")
    else:
        print("Employee not found.")

def sort_employees(employees: SortableDictionaryList):
    if employees.__len__() == 0:
        print("No employees in the system.")
    else:
        parameter = input("Select the parameter on which you want to sort the list: name, age, department or salary (default: name): ")
        order = input("Select the order on which you want to sort the list: asc or desc (default: asc): ")
        
        parameter = parameter if len(parameter) > 0 else "name"
        order = True if order == "desc" else False
        employees.sort(parameter, order)
        
        display_employees(employees)

    return None

def main():
    employees = SortableDictionaryList()

    employees.append(Employee(name="Erick", age=25, department="DEVELOP", salary=1300))
    employees.append(Employee(name="Karen", age=24, department="ACCOUNTING", salary=2100))
    employees.append(Employee(name="Jahir", age=26, department="IT", salary=2500))

    print(employees.__len__())
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Sort Employees")
        print("3. Display Employees")
        print("4. Update Employee")
        print("5. Remove Employee")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            sort_employees(employees)
        elif choice == '3':
            display_employees(employees)
        elif choice == '4':
            update_employee(employees)
        elif choice == '5':
            remove_employee(employees)
        elif choice == '6':
            break
        else:
            print("Invalid choice. try again.")

    print("Thank you for using This Management System!")

if __name__ == '__main__':
    main()