from file_methods import create_file_if_not_exist, add_contact, delete_contact, update_contact, search_contact

create_file_if_not_exist()


def main():
    app_running = True
    while app_running:
        print("\n Contact Management Book")
        print("1) Add Contact")
        print("2) Delete Contact")
        print("3) Update Contact")
        print("4) Search Contact")

        option = input("Enter the number with your desired option: ")

        if option == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            add_contact(name, phone, email, address)
        elif option == "2":
            name = input("Enter the name that you want to delete it's related contact: ")
            delete_contact(name)
        elif option == "3":
            name = input("Enter the name you want to update: ")
            search_contact(name)
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email: ")
            address = input("Enter the new address: ")
            update_contact(name, phone, email, address)
        elif option == "4":
            name = input("Enter the name you want search for: ")
            search_contact(name)


if __name__ == "__main__":
    main()
