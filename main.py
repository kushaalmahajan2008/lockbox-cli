from logic import add_new_password, password_generator, search_password,list_services
print("Welcome to Lockbox CLI version")


def show_menu():
    print("\nLockBox CLI")
    print("1. Add new password")
    print("2. Search password")
    print("3. Generate password")
    print("4. Get List of services")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_new_password()

        elif choice == "2":
            search_password()

        elif choice == "3":
            password=password_generator()
            print(f"\nGenerated Password:\n{password}")

        elif choice == "4":
            list_services()

        elif choice == "5":
            print("\nExiting LockBox. Stay secure.")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__=="__main__":
    main()