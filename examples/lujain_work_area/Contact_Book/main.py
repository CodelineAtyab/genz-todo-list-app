# todo_list_services.py

import csv
import re
from contact_book import ContactBook

def read_contact_records(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

def validate_phone(phone):
    # Regular expression for validating phone numbers with optional area code and separator
    phone_pattern = r'^(\+\d{1,3})?[-\s]?\d{3,}[-\s]?\d{3,}$'
    return re.match(phone_pattern, phone) is not None

def validate_email(email):
    # Regular expression for validating email addresses
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)

def validate_name(name):
    # Name should contain both first name and last name
    return ' ' in name.strip()

def main():
    contact_book = ContactBook("contact_records.csv")

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. View Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            while not validate_name(name):
                print("Invalid name. Please include both first name and last name.")
                name = input("Enter name: ")
            phone = input("Enter phone: ")
            while not validate_phone(phone):
                print("Invalid phone number format.")
                phone = input("Enter phone: ")
            email = input("Enter email: ")
            while not validate_email(email):
                print("Invalid email address format.")
                email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
            print("Contact added successfully.")

        elif choice == '2':
            identifier = input("Enter name, email, or phone of contact to delete: ")
            confirmation = input("Are you sure you want to delete contact? (yes/no): ")
            if confirmation.lower() == "yes":
                contact_book.delete_contact(identifier)
                print("Contact deleted successfully.")
            else:
                print("Deletion canceled.")

        elif choice == '3':
            identifier = input("Enter name, email, or phone of contact to update: ")
            new_phone = input("Enter new phone (leave empty to skip): ")
            while new_phone and not validate_phone(new_phone):
                print("Invalid phone number format.")
                new_phone = input("Enter new phone (leave empty to skip): ")
            new_email = input("Enter new email (leave empty to skip): ")
            while new_email and not validate_email(new_email):
                print("Invalid email address format.")
                new_email = input("Enter new email (leave empty to skip): ")
            new_address = input("Enter new address (leave empty to skip): ")
            contact_book.update_contact(identifier, new_phone, new_email, new_address)
            print("Contact updated successfully.")

        elif choice == '4':
            identifier = input("Enter name, email, or phone of contact to search: ")
            results = contact_book.search_contact(identifier)
            if results:
                for contact in results:
                    print(contact)
            else:
                print("No contacts found.")

        elif choice == '5':
            print("\nAll Contacts:")
            read_contact_records("contact_records.csv")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

