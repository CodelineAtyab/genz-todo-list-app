from ContactBook import ContactBook
from Contact import Contact


class TXTContactBook(ContactBook):
    def load_contacts(self, filename="contacts.txt"):
        with open(filename, 'r') as file:
            self.contacts = [Contact(*line.strip().split(", ")) for line in file]

    def save_contacts(self, filename="contacts.txt"):
        with open(filename, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact.name}, {contact.phone}, {contact.email}, {contact.address}\n")

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
