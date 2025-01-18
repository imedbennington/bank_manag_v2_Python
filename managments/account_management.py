class AccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_id = input("Enter Account ID: ")
        balance = float(input("Enter Initial Balance: "))
        self.accounts[acc_id] = balance
        print(f"Account {acc_id} created successfully.")

    def view_account(self):
        acc_id = input("Enter Account ID: ")
        if acc_id in self.accounts:
            print(f"Account ID: {acc_id}, Balance: {self.accounts[acc_id]}")
        else:
            print("Account not found.")

    def update_account(self):
        acc_id = input("Enter Account ID: ")
        if acc_id in self.accounts:
            new_balance = float(input("Enter New Balance: "))
            self.accounts[acc_id] = new_balance
            print(f"Account {acc_id} updated successfully.")
        else:
            print("Account not found.")

    def delete_account(self):
        acc_id = input("Enter Account ID: ")
        if acc_id in self.accounts:
            del self.accounts[acc_id]
            print(f"Account {acc_id} deleted successfully.")
        else:
            print("Account not found.")

    def list_accounts(self):
        if self.accounts:
            print("\n--- Account List ---")
            for acc_id, balance in self.accounts.items():
                print(f"Account ID: {acc_id}, Balance: {balance}")
        else:
            print("No accounts available.")
