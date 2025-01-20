class Account:
    def __init__(self, account_id, balance=0.0):
        self.account_id = account_id
        self._balance = balance  # Protected member

    @property #access functions like an attribute without parentheses.
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds or invalid amount")

    def __str__(self):
        return f"Account({self.account_id}, Balance: {self._balance})"


class SavingsAccount(Account):
    def __init__(self, account_id, balance=0.0, interest_rate=0.02):
        super().__init__(account_id, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self._balance += self._balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self, account_id, balance=0.0, overdraft_limit=500):
        super().__init__(account_id, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and self._balance - amount >= -self.overdraft_limit:
            self._balance -= amount
        else:
            raise ValueError("Exceeds overdraft limit or invalid amount")


class BusinessAccount(Account):
    def __init__(self, account_id, balance=0.0, loan_limit=10000):
        super().__init__(account_id, balance)
        self.loan_limit = loan_limit

    def request_loan(self, amount):
        if 0 < amount <= self.loan_limit:
            self._balance += amount
        else:
            raise ValueError("Loan amount exceeds limit")


class AccountManager:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts by account_id
    def create_account(self):
        print("\nSelect Account Type:")
        print("1. Savings Account")
        print("2. Checking Account")
        print("3. Business Account")
    
        acc_type = input("Enter account type (1/2/3): ").strip()

        acc_id = input("Enter Account ID: ").strip()
        initial_balance = float(input("Enter Initial Balance: "))

        if acc_id in self.accounts:
            print("Account ID already exists!")
            return

        # Create the account based on the selected type
        if acc_type == "1":
            account = SavingsAccount(acc_id, initial_balance)
            print(f"Savings Account {acc_id} created successfully.")
        elif acc_type == "2":
            account = CheckingAccount(acc_id, initial_balance)
            print(f"Checking Account {acc_id} created successfully.")
        elif acc_type == "3":
            account = BusinessAccount(acc_id, initial_balance)
            print(f"Business Account {acc_id} created successfully.")
        else:
            print("Invalid account type selected!")
            return  # Exit without saving the account if the type is invalid

        # Save the account in the dictionary
        self.accounts[acc_id] = account



    def view_account(self):
        acc_id = input("Enter account ID: ")
        account = self.accounts.get(acc_id)
        if account:
            print(account)
        else:
            print("Account not found!")

    def update_account(self):
        acc_id = input("Enter account ID: ")
        account = self.accounts.get(acc_id)
        if account:
            print("\nUpdate Options:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Add Interest (Savings Account only)")
            print("4. Request Loan (Business Account only)")
            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                    print(f"Deposited {amount}. New balance: {account.balance}")
                elif choice == "2":
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                    print(f"Withdrew {amount}. New balance: {account.balance}")
                elif choice == "3" and isinstance(account, SavingsAccount):
                    account.add_interest()
                    print(f"Interest added. New balance: {account.balance}")
                elif choice == "4" and isinstance(account, BusinessAccount):
                    amount = float(input("Enter loan amount: "))
                    account.request_loan(amount)
                    print(f"Loan of {amount} approved. New balance: {account.balance}")
                else:
                    print("Invalid choice or not applicable for this account type!")
            except ValueError as e:
                print(e)
        else:
            print("Account not found!")

    def delete_account(self):
        acc_id = input("Enter account ID: ")
        if acc_id in self.accounts:
            del self.accounts[acc_id]
            print(f"Account {acc_id} deleted successfully!")
        else:
            print("Account not found!")

    def list_accounts(self):
        if self.accounts:
            print("\n--- List of Accounts ---")
            for account in self.accounts.values():
                print(account)
        else:
            print("No accounts available!")


def account_management_menu(acc_manager):
    while True:
        print("\n--- Account Management Menu ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Update Account")
        print("4. Delete Account")
        print("5. List All Accounts")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            acc_manager.create_account()
        elif choice == "2":
            acc_manager.view_account()
        elif choice == "3":
            acc_manager.update_account()
        elif choice == "4":
            acc_manager.delete_account()
        elif choice == "5":
            acc_manager.list_accounts()
        elif choice == "6":
            print("Exiting Account Management. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


