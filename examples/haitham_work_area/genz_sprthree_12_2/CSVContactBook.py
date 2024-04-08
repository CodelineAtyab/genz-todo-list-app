import csv
from ContactBook import ContactBook
from Contact import Contact


class CSVContactBook(ContactBook):
    def load_contacts(self, filename="contacts.csv"):
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            self.contacts = [Contact(row['name'], row['phone'], row['email'], row['address']) for row in reader]

    def save_contacts(self, filename="contacts.csv"):
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['name', 'phone', 'email', 'address']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({'name': contact.name, 'phone': contact.phone, 'email': contact.email, 'address': contact.address})

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)

    def delete_contact(self, email):
        self.contacts = [contact for contact in self.contacts if contact.email != email]

    def update_contact(self, email, name=None, phone=None, new_email=None, address=None):
        for contact in self.contacts:
            if contact.email == email:
                contact.name = name if name is not None else contact.name
                contact.phone = phone if phone is not None else contact.phone
                contact.email = new_email if new_email is not None else contact.email
                contact.address = address if address is not None else contact.address
                break

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
