import file_manager

"""
This py file is the main file of this program, takes user inputs and sends them to the 
file manager for processing.
"""


def main():
    running = True  # stores the state of the application whether it's running or not
    file_manager.if_header_exists()  # Calls the header function which creates a header for the csv file
    while running:
        print("(1) Add contact")
        print("(2) Delete contact")
        print("(3) Update Contact")
        print("(4) Search Contact")
        print("(5) Exit")

        try:
            choice = int(input("Enter chosen operation: "))
        except Exception as ex:
            print("Error, Try again.", ex)
            choice = int(input("Enter chosen operation: "))

        if choice == 1:
            add_name, add_contact, add_email, add_address = enter_contact()
            file_manager.store_contact(add_name, add_contact, add_email, add_address)

        elif choice == 2:
            delete = input("input desired item to be deleted by phone number: ")
            file_manager.delete_contact(delete)

        elif choice == 3:
            old_info = input("Enter the exact phone number of the field you wish to update: ")
            add_name, add_contact, add_email, add_address = enter_contact()
            file_manager.update_contact(old_info, add_name, add_contact, add_email, add_address)

        elif choice == 4:
            search = input("Enter search Number: ")
            print(file_manager.read_contact(search))

        elif choice == 5:
            print("Closing")
            running = False


def enter_contact():
    add_name = input("Enter contact name: ")
    add_contact = input("Enter contact num: ")
    add_email = input("Enter contact email: ")
    add_address = input("Enter contact address: ")
    return add_name, add_contact, add_email, add_address


if __name__ == "__main__":
    main()
