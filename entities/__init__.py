# Import classes from account.py and person.py for direct access
from .account import Account, SavingsAccount, CheckingAccount, BusinessAccount
from .person import Person, Client, Employee
from .department import Department
# Expose these classes when importing models
__all__ = ["Account", "SavingsAccount", "CheckingAccount", "BusinessAccount", "Person", "Client", "Employee", "Department"]
