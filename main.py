from service.bank_services import Bank
from entities.account import SavingsAccount, CheckingAccount, BusinessAccount, AccountManager
from entities.person import Client, Employee
from entities.department import Department, DepartmentManager
from managments.account_management import AccountManager
from managments.account_menu import account_management_menu
from managments.clients_management import ClientManagement
from managments.employee_management import EmployeeManagement
def display_menu():
    print("\n--- Bank Management System ---")
    print("1. Manage clients")
    print("2. Add Employee")
    print("3. Manage accounts")
    print("4. List Clients")
    print("5. List Employees")
    print("6. Manage Departments")
    print("7. Exit")
    print("-----------------------------")


def main():
    bank = Bank()
    dep_manager = DepartmentManager()  # Instantiate DepartmentManager
    acc_manager = AccountManager()
    client_manager = ClientManagement()
    departments = [dept.value for dept in Department]  # List of valid departments
    accounts = {}  # Dictionary to store accounts by account number

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":  # Add Client
            """client_id = input("Enter client ID: ")
            passport_number = input("Enter passport number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            client = Client(first_name, last_name, passport_number, client_id)
            bank.add_client(client)
            print(f"Client {first_name} {last_name} added successfully!")"""
            client_manager.menu()

        elif choice == "2":  # Add Employee
            first_name = input("Enter employee first name: ")
            last_name = input("Enter employee last name: ")
            emp_id = input("Enter employee ID: ")
            emp_code = input("Enter employee code: ")
            salary = float(input("Enter employee salary: "))
            department = input(f"Enter department ({', '.join(departments)}): ")

            try:
                employee = Employee(emp_id, first_name, last_name, salary, emp_code, department)
                bank.add_employee(employee)
                print(f"Employee {first_name} {last_name} added successfully!")
            except ValueError as e:
                print(e)

        elif choice == "3":  # Create Account
            """print("Select Account Type:")
            print("1. Savings Account")
            print("2. Checking Account")
            print("3. Business Account")
            acc_choice = input("Enter account type: ")
            acc_number = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))

            if acc_choice == "1":
                account = SavingsAccount(acc_number, balance)
            elif acc_choice == "2":
                account = CheckingAccount(acc_number, balance)
            elif acc_choice == "3":
                account = BusinessAccount(acc_number, balance)
            else:
                print("Invalid account type selected!")
                continue

            accounts[acc_number] = account
            print(f"Account {acc_number} created successfully!")"""
            
            account_management_menu(acc_manager)

        elif choice == "4":  # List Clients
            print("\n--- Client List ---")
            bank.list_clients()

        elif choice == "5":  # List Employees
            print("\n--- Employee List ---")
            bank.list_employees()

        elif choice == "6":  # Manage Departments
            dep_manager.department_menu()

        elif choice == "7":  # Exit
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
