import csv
import json
from ContactBook import ContactBook
from ContactRecord import ContactRecord
from AbstractConactBook import AbstractContactBook

class AppUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.contact_book = ContactBook()

    def save_contact_book(self, file_path):
        self.contact_book.save_to_file(file_path)

    def load_contact_book(self, file_path):
        self.contact_book.load_from_file(file_path)

def main():
    user = AppUser("Ahmed", "Ahmed@example.com")
    
    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. Save Contact Book to File")
        print("6. Load Contact Book from File")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact = ContactRecord(name, phone, email, address)
            user.contact_book.add_contact(contact)
            print("Contact added successfully.")

        elif choice == '2':
            identifier = input("Enter Email of contact to delete: ")
            user.contact_book.delete_contact(identifier)
            print("Contact deleted successfully.")

        elif choice == '3':
            identifier = input("Enter Email of contact to update: ")
            contact = user.contact_book.search_contact(identifier)
            if contact:
                new_name = input("Enter new Name (press Enter to skip): ")
                new_phone = input("Enter New Phone (press Enter to skip): ")
                new_email = input("Enter New Email (press Enter to skip): ")
                new_address = input("Enter New Address (press Enter to skip): ")
                if new_name or new_phone or new_email or new_address:
                    new_contact = ContactRecord(new_name or contact.name, 
                                                new_phone or contact.phone, 
                                                new_email or contact.email, 
                                                new_address or contact.address)
                    user.contact_book.update_contact(identifier, new_contact)
                    print("Contact updated successfully.")
                else:
                    print("No changes made.")
            else:
                print("Contact not found.")

        elif choice == '4':
            identifier = input("Enter contacts Email to search: ")
            contact = user.contact_book.search_contact(identifier)
            if contact:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("Contact not found.")

        elif choice == '5':
            file_path = input("Enter file path to save the Contact Book(with the file extension): ")
            user.save_contact_book(file_path)
            print("Contact Book saved successfully.")

        elif choice == '6':
            file_path = input("Enter file path to load the Contact Book(with the file extension): ")
            user.load_contact_book(file_path)
            print("Contact Book loaded successfully.")

        elif choice == '7':
            print("Done")
            break

        else:
            print("Invalid choice. Please Select from 1-7")

if __name__ == "__main__":
    main()
