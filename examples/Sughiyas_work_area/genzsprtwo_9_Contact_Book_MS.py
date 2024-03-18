import csv
import os

# Specify the path to the "Sughiyas_work_area" directory
DIRECTORY = "Sughiyas_work_area"

# Create the "Sughiyas_work_area" directory if it doesn't exist
os.makedirs(DIRECTORY, exist_ok=True)

# Define the path to the CSV file
CONTACTS_FILE = os.path.join(DIRECTORY, "./contacts.csv")

FIELDNAMES = ['Name', 'Phone', 'Email', 'Address']

def load_contacts():
    file_path = "./contacts.csv"
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(name, phone, email, address):
    # contacts = load_contacts()
    contacts = []
    contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
    save_contacts(contacts)
    print("Contact added successfully.")

def delete_contact(identifier):
    contacts = load_contacts()
    for contact in contacts:
        if contact['Name'] == identifier or contact['Email'] == identifier:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def update_contact(identifier, new_phone=None, new_email=None, new_address=None):
    contacts = load_contacts()
    for contact in contacts:
        if contact['Email'] == identifier:
            if new_phone:
                contact['Phone'] = new_phone
            if new_email:
                contact['Email'] = new_email
            if new_address:
                contact['Address'] = new_address
            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def search_contact(identifier):
    contacts = load_contacts()
    for contact in contacts:
        if contact['Name'] == identifier or contact['Email'] == identifier or contact['Phone'] == identifier:
            print(f"{contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nContact Book Management System")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            add_contact(name, phone, email, address)

        elif choice == '2':
            identifier = input("Enter Name or Email of contact to delete: ")
            delete_contact(identifier)

        elif choice == '3':
            identifier = input("Enter Email of contact to update: ")
            new_phone = input("Enter New Phone (press Enter to skip): ")
            new_email = input("Enter New Email (press Enter to skip): ")
            new_address = input("Enter New Address (press Enter to skip): ")
            update_contact(identifier, new_phone, new_email, new_address)

        elif choice == '4':
            identifier = input("Enter Name, Email, or Phone of contact to search: ")
            search_contact(identifier)

        elif choice == '5':
            print("Done")
            break

        else:
            print("Invalid choice. Please Select from 1-5")

if __name__ == "__main__":
    main()
