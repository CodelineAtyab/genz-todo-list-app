from OOP_contact_record import ContactRecord
from OOP_contact import ContactBook


def main():
    running = True  # stores the state of the application whether it's running or not
    contact_book = ContactBook(storage_format="csv")
    contact_book.if_header_exists()  # Calls the header function which creates a header for the csv file

    while running:
        print("(1) Add contact")
        print("(2) Load in chosen format")
        print("(3) Update Contact")
        print("(4) Search Contact")
        print("(5) Delete Contact")
        print("(6) Exit")

        try:
            choice = int(input("Enter chosen operation: "))
        except Exception as ex:
            print("Error, Try again.", ex)
            choice = int(input("Enter chosen operation: "))

        if choice == 1:  # takes user input and adds a contact record
            add_name, add_contact, add_email, add_address = enter_contact()
            contact_book.store_contact(add_name, add_contact, add_email, add_address)

        elif choice == 2:  # loads data in chosen format
            print("Select new storage format:")
            print("1. CSV")
            print("2. TXT")
            print("3. JSON")
            format_choice = input("Enter the number of the desired storage format: ")

            if format_choice == '1':
                new_format = 'csv'
            elif format_choice == '2':
                new_format = 'txt'
            elif format_choice == '3':
                new_format = 'json'
            else:
                print("Invalid choice, defaulting to CSV format.")
                new_format = 'csv'

            contact_book.load_contacts(new_format)
            running = False

        elif choice == 3:  # Update a record
            old_info = input("Enter the exact phone number of the field you wish to update: ")
            add_name, add_contact, add_email, add_address = enter_contact()
            contact_book.update_contact(old_info, add_name, add_contact, add_email, add_address)

        elif choice == 4:  # search for a contact
            search = input("Enter search Number: ")
            print(contact_book.read_contact(search))

        elif choice == 5:  # Delete contact
            delete = input("input desired item to be deleted by phone number: ")
            contact_book.delete_contact(delete)


def enter_contact():
    add_name = input("Enter contact name: ")
    add_contact = input("Enter contact num: ")
    add_email = input("Enter contact email: ")
    add_address = input("Enter contact address: ")
    return add_name, add_contact, add_email, add_address


if __name__ == "__main__":
    main()
