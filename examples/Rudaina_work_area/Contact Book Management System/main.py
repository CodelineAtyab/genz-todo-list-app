import file_manager


def main():
    app_running = True
    while app_running:
        print("---------------------------------")
        print("Contact Book Management System: ")
        print("(1) Add.")
        print("(2) Delete.")
        print("(3) Update.")
        print("(4) Search.")
        print("(5) Exit.")

        user_input = input("Please select one of the options: ")
        if user_input and user_input.isdigit():
            choice = int(user_input)

            if choice == 1:  # Add
                row = []
                name_input = input("Name: ")
                row.append(name_input)
                phone_input = input("Phone: ")
                row.append(phone_input)
                email_input = input("Email: ")
                row.append(email_input)
                addr_input = input("Address: ")
                row.append(addr_input)
                file_manager.append_contact(row, True)

            elif choice == 2:  # delete
                print("Give us one of your existing contact info\n"
                      "(0)Name (1)Phone (2)Email\n")
                try:
                    delete_identifier = int(input("Your Choice: "))
                    delete_data = input("Enter the contact: ")
                    file_manager.delete_contact_data(delete_identifier, delete_data)
                except ValueError:
                    print("Error: Please enter an integer.")

            if choice == 3:  # Update
                original = input("Enter the Contact Name: ")
                file_manager.search(0, original)
                print("What do you want to update?")
                print("(0) Name, (1) Phone, (2) Email, (3) Address ")
                try:
                    identifier = int(input("Your Choice: "))
                    updated = input("Enter the updated contact: ")
                    file_manager.update(identifier, original, updated)
                except ValueError:
                    print("Error: Please enter an integer.")

            if choice == 4:  # Search
                print("Give us one of your existing contact info\n"
                      "(0)Name\n(1)Phone\n(2)Email\n")
                try:
                    search_identifier = int(input("Your Choice: "))
                    searched_data = input("Enter the information: ")
                    file_manager.search(search_identifier, searched_data)
                except ValueError:
                    print("Error: Please enter an integer.")

            if choice == 5:  # Exit
                app_running = False

        else:
            print("Wrong choice")


if __name__ == "__main__":
  main()
