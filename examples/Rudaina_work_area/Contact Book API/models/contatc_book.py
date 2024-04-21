from abc import ABC, abstractmethod
import json
from models.contact_record import ContactRecord


class ContactBook(ABC):

    user_contact_records = {}  # Dictionary to store user email and associated ContactRecord

    def __init__(self, owner, user_email):
        self.owner = owner
        self.contacts = []
        self.user_email = user_email
        self.user_contact_records.setdefault(user_email, [])  # Initialize list for the user's contacts

    @abstractmethod
    def load_contact_data(self):
        pass

    @abstractmethod
    def save_contact(self):
        pass

    def add(self, contact):
        self.contacts.append(contact)

    def delete(self, email):
        self.contacts = [contact for contact in self.contacts if contact.get_email() != email]

    def update(self, name, updated_contact):
        for i, contact in enumerate(self.contacts):
            if contact.get_name() == name:
                self.contacts[i] = updated_contact

    def search(self, email):
        for contact in self.contacts:
            if contact.get_email() == email:
                return contact
        return None


class JsonContactBook(ContactBook):
    json_file = './contact_book.json'

    def load_contact_data(self):
        file_path = f"{self.user_email}.json"
        # file_path = './data/contacts.json'
        with open(file_path, 'r') as file:
            data = json.load(file)
            contacts = []
        for contact_data in data:
            contact = ContactRecord(**contact_data)
            contacts.append(contact)
        return contacts

    def save_contact(self):
        file_path = f"{self.user_email}.json"
        with open(file_path, 'w') as file:
            json.dump([vars(contact) for contact in self.contacts], file, indent=4)


class TxtContactBook(ContactBook):
    def load_contact_data(self, file_path):
        contacts = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                # Split each line by comma to extract contact information
                contact_info = line.strip().split(',')
                if len(contact_info) >= 4:
                    # Create a ContactRecord object from the contact information
                    contact = ContactRecord(contact_info[0], contact_info[1], contact_info[2], contact_info[3])
                    contacts.append(contact)
        return contacts

    def save_contact(self, contacts):
        file_path = f"{self.user_email}.txt"
        with open(file_path, 'w') as file:
            for contact in contacts:
                # Write each contact's information to a new line in the text file
                file.write(f"{contact.get_name()}, {contact.get_phone_number()}, {contact.get_email()}, {contact.get_address()}\n")



