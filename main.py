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
    print("2. Manage Employees")
    print("3. Manage accounts")
    print("4. Manage Departments")
    print("5. Exit")
    print("-----------------------------")


def main():
    bank = Bank()
    dep_manager = DepartmentManager()  # Instantiate DepartmentManager
    emp_manager = EmployeeManagement()
    client_manager = ClientManagement()
    account_manager = AccountManager(client_manager)  # Pass client_manager to AccountManager
    departments = [dept.value for dept in Department]  # List of valid departments
    accounts = {}  # Dictionary to store accounts by account number

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":  # Manage clients
            client_manager.menu()

        elif choice == "2":  # Manage employees
            emp_manager.menu()

        elif choice == "3":  # Manage accounts
            account_manager.menu()

        elif choice == "4":  # Manage Departments
            dep_manager.department_menu()

        elif choice == "5":  # Exit
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
