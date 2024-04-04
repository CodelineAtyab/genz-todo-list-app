import csv
import json

class AbstractContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, email):
        self.contacts = [c for c in self.contacts if c.email != email]

    def update_contact(self, email, new_contact):
        for idx, contact in enumerate(self.contacts):
            if contact.email == email:
                self.contacts[idx] = new_contact

    def search_contact(self, email):
        for contact in self.contacts:
            if contact.email == email:
                return contact
        return None

    def save_to_file(self, file_path):
        raise NotImplementedError("Subclasses must implement save_to_file method")

    def load_from_file(self, file_path):
        raise NotImplementedError("Subclasses must implement load_from_file method")