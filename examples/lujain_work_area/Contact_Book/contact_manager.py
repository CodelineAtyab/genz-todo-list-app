# contact_manager.py

import csv
import os
import re

# Defines ContactRecord class to represent a single contact record
class ContactRecord:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    # Converts ContactRecord object to dictionary
    def to_dict(self):
        return {'Name': self.name, 'Phone': self.phone, 'Email': self.email, 'Address': self.address}

# Defines ContactBook class to manage contacts
class ContactBook:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fieldnames = ['Name', 'Phone', 'Email', 'Address']
        self.contacts = self.load_contacts()

    # Loads contacts from CSV file
    def load_contacts(self):
        if not os.path.exists(self.csv_file):
            return []
        with open(self.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    # Saves contacts to CSV file
    def save_contacts(self):
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.contacts)

    # Adds a new contact to the contact list
    def add_contact(self, contact):
        self.contacts.append(contact.to_dict())  # Converts ContactRecord object to dictionary before appending
        self.save_contacts()

    # Deletes a contact from the contact list
    def delete_contact(self, identifier):
        self.contacts = [contact for contact in self.contacts if contact['Name'] != identifier and
                         contact['Email'] != identifier and contact['Phone'] != identifier]
        self.save_contacts()

    # Updates a contact in the contact list
    def update_contact(self, identifier, new_contact):
        for contact in self.contacts:
            if contact['Name'] == identifier or contact['Email'] == identifier or contact['Phone'] == identifier:
                contact.update(new_contact)
        self.save_contacts()

    # Searches for contacts based on the given identifier
    def search_contact(self, identifier):
        results = []
        for contact in self.contacts:
            if contact['Name'] == identifier or contact['Email'] == identifier or contact['Phone'] == identifier:
                results.append(contact)
        return results

# Functions to read contact records from CSV file
def read_contact_records(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

# Regular expression for validating phone numbers with optional area code and separator
def validate_phone(phone):
    phone_pattern = r'^(\+\d{1,3})?[-\s]?\d{3,}[-\s]?\d{3,}$'
    return re.match(phone_pattern, phone) is not None

# Regular expression for validating email addresses
def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)

# Name should contain both first name and last name
def validate_name(name):
    return ' ' in name.strip()

# Main function to manage the contact book application
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
            contact = ContactRecord(name, phone, email, address)
            contact_book.add_contact(contact)
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
            new_contact = {}
            if new_phone:
                new_contact['Phone'] = new_phone
            if new_email:
                new_contact['Email'] = new_email
            if new_address:
                new_contact['Address'] = new_address
            contact_book.update_contact(identifier, new_contact)
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
