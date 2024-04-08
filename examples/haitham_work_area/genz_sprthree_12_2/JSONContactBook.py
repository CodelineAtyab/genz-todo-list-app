import json
from ContactBook import ContactBook
from Contact import Contact


class JSONContactBook(ContactBook):
    def load_contacts(self, filename="contacts.json"):
        with open(filename, 'r') as file:
            contacts_list = json.load(file)
            self.contacts = [Contact(**contact) for contact in contacts_list]

    def save_contacts(self, filename="contacts.json"):
        with open(filename, 'w') as file:
            json.dump([contact.__dict__ for contact in self.contacts], file, indent=4)

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
