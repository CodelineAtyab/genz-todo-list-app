from abc import ABC, abstractmethod
from Contact import Contact


class ContactBook(ABC):
    def __init__(self):
        self.contacts = []

    @abstractmethod
    def load_contacts(self, filename):
        pass

    @abstractmethod
    def save_contacts(self, filename):
        pass

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def find_contact(self, email):
        for contact in self.contacts:
            if contact.email == email:
                return contact
        return None

    def delete_contact(self, email):
        contact = self.find_contact(email)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def update_contact(self, email, name=None, phone=None, new_email=None, address=None):
        contact = self.find_contact(email)
        if contact:
            contact.name = name if name else contact.name
            contact.phone = phone if phone else contact.phone
            contact.email = new_email if new_email else contact.email
            contact.address = address if address else contact.address
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(contact)
