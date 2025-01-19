from entities.person import Client
from entities.account import Account

class ClientManagement:
    def __init__(self):
        self.clients = []

    def add_client(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        id_number = input("Enter ID number: ")
        passport_number = input("Enter passport number: ")
        client = Client(first_name, last_name, passport_number, id_number)
        self.clients.append(client)
        print("Client added successfully!")

    def view_clients(self):
        if not self.clients:
            print("No clients available.")
            return
        for client in self.clients:
            print(client)

    def find_client(self):
        id_number = input("Enter client ID to search: ")
        client = next((c for c in self.clients if c.id_number == id_number), None)
        if client:
            print(client)
        else:
            print("Client not found.")

    def delete_client(self):
        id_number = input("Enter client ID to delete: ")
        client = next((c for c in self.clients if c.id_number == id_number), None)
        if client:
            self.clients.remove(client)
            print("Client removed successfully.")
        else:
            print("Client not found.")

    def menu(self):
        while True:
            print("\nClient Management Menu")
            print("1. Add Client")
            print("2. View Clients")
            print("3. Find Client")
            print("4. Delete Client")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_client()
            elif choice == "2":
                self.view_clients()
            elif choice == "3":
                self.find_client()
            elif choice == "4":
                self.delete_client()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
