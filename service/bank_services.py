from entities.account import SavingsAccount, CheckingAccount, BusinessAccount
from entities.person import Client, Employee

class Bank:
    def __init__(self):
        self.clients = []
        self.employees = []

    def add_client(self, client):
        self.clients.append(client)

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_clients(self):
        for client in self.clients:
            print(client)

    def list_employees(self):
        for employee in self.employees:
            print(employee)
