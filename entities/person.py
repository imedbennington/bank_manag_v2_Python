from .department import Department
class Person:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        return f"{self.name} ({self.id_number})"


class Client(Person):
    def __init__(self, first_name, last_name, passport_number, id_number, accounts=None):
        super().__init__(f"{first_name} {last_name}", id_number)
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number
        self.accounts = accounts if accounts else []

    def __str__(self):
        return (f"Client: {self.first_name} {self.last_name}, ID: {self.id_number}, "
                f"Passport: {self.passport_number}")

    def add_account(self, account):
        self.accounts.append(account)

    def total_balance(self):
        return sum(account.balance for account in self.accounts)


class Employee(Person):
    def __init__(self, id_number, first_name, last_name, salary, employee_id, department):
        super().__init__(first_name, last_name , id_number)
        self.employee_id = employee_id
        self.salary = salary
        if department.upper() not in Department.__members__:
            raise ValueError(f"Invalid department: {department}. Must be one of {list(Department.__members__.keys())}.")
        self.department = Department[department.upper()]
    def __str__(self):
        return (f"Employee(ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, "
                f"Salary: {self.salary}, Department: {self.department.value})")
