from entities.person import Employee

class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        id_number = input("Enter ID number: ")
        employee_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))
        department = input("Enter department (HR, IT, FINANCE, MARKETING): ")
        try:
            employee = Employee(id_number, first_name, last_name, salary, employee_id, department)
            self.employees.append(employee)
            print("Employee added successfully!")
        except ValueError as e:
            print(e)

    def view_employees(self):
        if not self.employees:
            print("No employees available.")
            return
        for emp in self.employees:
            print(emp)

    def find_employee(self):
        employee_id = input("Enter employee ID to search: ")
        employee = next((e for e in self.employees if e.employee_id == employee_id), None)
        if employee:
            print(employee)
        else:
            print("Employee not found.")

    def delete_employee(self):
        employee_id = input("Enter employee ID to delete: ")
        employee = next((e for e in self.employees if e.employee_id == employee_id), None)
        if employee:
            self.employees.remove(employee)
            print("Employee removed successfully.")
        else:
            print("Employee not found.")

    def menu(self):
        while True:
            print("\nEmployee Management Menu")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Find Employee")
            print("4. Delete Employee")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.find_employee()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
