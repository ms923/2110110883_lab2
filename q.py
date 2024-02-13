class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def print_table(self):
        print("EID\tName\tAge\tSalary (PM)")
        for employee in self.employees:
            print(employee)

    def sort_table(self, key):
        self.employees.sort(key=lambda x: getattr(x, key))

def main():
    employees = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000)
    ]

    employee_table = EmployeeTable(employees)

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        employee_table.sort_table("age")
    elif choice == 2:
        employee_table.sort_table("name")
    elif choice == 3:
        employee_table.sort_table("salary")
    else:
        print("Invalid choice. Sorting by default parameter (Employee ID).")
        employee_table.sort_table("emp_id")

    print("\nSorted Employee Table:")
    employee_table.print_table()

if __name__ == "__main__":
    main()
