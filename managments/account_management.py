from entities.person import Client
from entities.account import SavingsAccount, CheckingAccount, BusinessAccount


class AccountManager:
    def __init__(self, client_manager):
        self.accounts = {}  # Stores accounts by account_id
        self.client_manager = client_manager  # Reference to ClientManagement instance

    def create_account(self):
        print("\nSelect Account Type:")
        print("1. Savings Account")
        print("2. Checking Account")
        print("3. Business Account")

        acc_type = input("Enter account type (1/2/3): ").strip()
        acc_id = input("Enter Account ID: ").strip()
        client_id = input("Enter Client ID: ").strip()

        # Validate that the client exists
        client = next((c for c in self.client_manager.clients if c.id_number == client_id), None)
        if not client:
            print("Client does not exist! Add the client first.")
            return

        initial_balance = float(input("Enter Initial Balance: "))

        if acc_id in self.accounts:
            print("Account ID already exists!")
            return

        # Create the account based on the selected type
        if acc_type == "1":
            account = SavingsAccount(acc_id, initial_balance)
            print(f"Savings Account {acc_id} created successfully for Client {client_id}.")
        elif acc_type == "2":
            account = CheckingAccount(acc_id, initial_balance)
            print(f"Checking Account {acc_id} created successfully for Client {client_id}.")
        elif acc_type == "3":
            account = BusinessAccount(acc_id, initial_balance)
            print(f"Business Account {acc_id} created successfully for Client {client_id}.")
        else:
            print("Invalid account type selected!")
            return

        # Save the account in the dictionary with client association
        self.accounts[acc_id] = {"account": account, "client": client}

    def list_accounts(self):
        if self.accounts:
            print("\n--- Account List ---")
            for acc_id, details in self.accounts.items():
                account = details["account"]
                client = details["client"]
                print(f"Account ID: {account.acc_id}, Balance: {account.balance}, Client: {client}")
        else:
            print("No accounts available.")

    def menu(self):
        while True:
            print("\nAccount Management Menu")
            print("1. Create Account")
            print("2. List Accounts")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.list_accounts()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
