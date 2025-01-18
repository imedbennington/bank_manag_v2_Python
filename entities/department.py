from enum import Enum

class Department(Enum):
    HR = "Human Resources"
    IT = "Information Technology"
    FINANCE = "Finance"
    SALES = "Sales"
    MARKETING = "Marketing"

# A dictionary to manage departments dynamically
department_dict = {dept.name: dept.value for dept in Department}

def add_department(code, name):
    if code.upper() in department_dict:
        raise ValueError(f"Department code '{code}' already exists.")
    department_dict[code.upper()] = name
    print(f"Department '{name}' added successfully!")

def view_departments():
    print("\nDepartments:")
    for code, name in department_dict.items():
        print(f"{code}: {name}")

def remove_department(code):
    if code.upper() not in department_dict:
        raise KeyError(f"Department code '{code}' not found.")
    removed = department_dict.pop(code.upper())
    print(f"Department '{removed}' removed successfully!")

class DepartmentManager:
    def department_menu(self):
        while True:
            print("\nDepartment Management")
            print("1. Add Department")
            print("2. View Departments")
            print("3. Remove Department")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                code = input("Enter department code (e.g., RND): ")
                name = input("Enter department name (e.g., Research and Development): ")
                try:
                    add_department(code, name)
                except ValueError as e:
                    print(e)

            elif choice == "2":
                view_departments()

            elif choice == "3":
                code = input("Enter department code to remove: ")
                try:
                    remove_department(code)
                except KeyError as e:
                    print(e)

            elif choice == "4":
                print("Exiting Department Management.")
                break

            else:
                print("Invalid choice. Please try again.")
