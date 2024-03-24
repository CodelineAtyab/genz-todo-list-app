import csv
import os

# Specify the path to the "Data" directory
DIRECTORY = "data"

# Create the "Data" directory if it doesn't exist
os.makedirs(DIRECTORY, exist_ok=True)

# Define the path to the CSV file
CONTACTS_FILE = os.path.join(DIRECTORY, "contacts.csv")

FIELDNAMES = ['Name', 'Phone', 'Email', 'Address']
if not os.path.exists(CONTACTS_FILE):
    with open(CONTACTS_FILE, 'w', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        csv_writer.writeheader()
else:
    with open(CONTACTS_FILE, 'a', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
    else:
        data = []

    return data

def save_contacts(contacts, op):
    if op=="add":
        with open(CONTACTS_FILE, 'a', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            csv_writer.writerow(contacts[-1])
    elif op=="delete":
        with open(CONTACTS_FILE, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            csv_writer.writeheader()
            csv_writer.writerows(contacts)
    elif op=="update":
        with open(CONTACTS_FILE, 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            csv_writer.writeheader()
            csv_writer.writerows(contacts)

def add_contact(name, phone, email, address):
    contacts = load_contacts()  # Load existing contacts
    contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
    save_contacts(contacts, "add")
    print("Contact added successfully.")

def delete_contact(identifier):
    contacts = load_contacts()
    for contact in contacts:
        if contact['Email'] == identifier:
            contacts.remove(contact)
            save_contacts(contacts, "delete")
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def update_contact(identifier, new_phone=None, new_email=None, new_address=None, new_name=None):
    contacts = load_contacts()
    for contact in contacts:
        if contact['Email'] == identifier:
            if new_name:
                contact['Name'] = new_name
            if new_phone:
                contact['Phone'] = new_phone
            if new_email:
                contact['Email'] = new_email
            if new_address:
                contact['Address'] = new_address
            print(contacts)
            save_contacts(contacts, "update")
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def search_contact(identifier):
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if contact['Email'].strip().lower() == identifier.strip().lower():
            found = True
            print(f"{contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")
            return      
    if not found:
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
            identifier = input("Enter Email of contact to delete: ")
            delete_contact(identifier)

        elif choice == '3':
            identifier = input("Enter Email of contact to update: ")
            new_name = input("Enter new Name (press Enter to skip): ")
            new_phone = input("Enter New Phone (press Enter to skip): ")
            new_email = input("Enter New Email (press Enter to skip): ")
            new_address = input("Enter New Address (press Enter to skip): ")
            update_contact(identifier, new_phone, new_email, new_address, new_name)

        elif choice == '4':
            identifier = input("Enter contacts Email to search: ")
            search_contact(identifier)

        elif choice == '5':
            print("Done")
            break

        else:
            print("Invalid choice. Please Select from 1-5")

if __name__ == "__main__":
    main()
