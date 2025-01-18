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
