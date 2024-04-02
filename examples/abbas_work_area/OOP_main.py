from OOP_contact_record import ContactRecord
from OOP_contact import ContactBook


def main():
    running = True  # stores the state of the application whether it's running or not
    contact_book = ContactBook()
    #file_manager.if_header_exists()  # Calls the header function which creates a header for the csv file

    # Determines users chosen file type
    print("Select storage format:")
    print("1. CSV")
    print("2. TXT")
    print("3. JSON")
    try:
        storage_format_choice = int(input("Enter the number of the desired storage format: "))
    except ValueError:
        print("Invalid input, defaulting to CSV format.")
        storage_format_choice = 1

    if storage_format_choice == 1:
        storage_format = 'csv'
    elif storage_format_choice == 2:
        storage_format = 'txt'
    elif storage_format_choice == 3:
        storage_format = 'json'
    else:
        print("Invalid choice, default CSV format.")
        storage_format = 'csv'

    contact_book = ContactBook(storage_format=storage_format)

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
            contact_book.store_contact(add_name, add_contact, add_email, add_address)


def enter_contact():
    add_name = input("Enter contact name: ")
    add_contact = input("Enter contact num: ")
    add_email = input("Enter contact email: ")
    add_address = input("Enter contact address: ")
    return add_name, add_contact, add_email, add_address


if __name__ == "__main__":
    main()
