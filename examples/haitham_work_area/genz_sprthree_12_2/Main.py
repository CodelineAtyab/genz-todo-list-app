from AppUser import AppUser
from CSVContactBook import CSVContactBook
from TXTContactBook import TXTContactBook
from JSONContactBook import JSONContactBook
from ContactBook import ContactBook
from Contact import Contact
from DownloadContactBook import *


def get_contact_details():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    return name, phone, email, address


def main():
    print("Welcome to the Contact Book Application!")
    username = input("Please enter your username: ")
    email = input("Please enter your email: ")
    user = AppUser(username, email)

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. List All Contacts")
        print("5. Download Contacts")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name, phone, email, address = get_contact_details()
            user.contact_book.add_contact(name, phone, email, address)
            print("Contact added successfully.")
        elif choice == '2':
            email = input("Enter the email of the contact to delete: ")
            user.contact_book.delete_contact(email)
        elif choice == '3':
            email = input("Enter the email of the contact to update: ")
            print("Enter new details (press enter to skip):")
            name, phone, new_email, address = get_contact_details()
            user.contact_book.update_contact(email, name, phone, new_email if new_email else None, address)
            print("Contact updated successfully.")
        elif choice == '4':
            user.contact_book.list_contacts()

        elif choice == "5":
            format_choice = input("Download as (CSV, TXT, JSON): ").upper()
            if format_choice == "CSV":
                ContactBook.save_contacts("contacts_export.csv")
                print("Contacts downloaded as CSV.")
            elif format_choice == "TXT":
                export_as_txt(ContactBook, "contacts_export.txt")
            elif format_choice == "JSON":
                export_as_json(ContactBook, "contacts_export.json")
            else:
                print("Invalid format selected.")

        elif choice == '6':
            print("Exiting the Contact Book Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
