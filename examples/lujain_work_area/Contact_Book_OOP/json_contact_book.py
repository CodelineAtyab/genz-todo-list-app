# json_contact_book.py

import json
from contact_book import AbstractContactBook
from contact_record import ContactRecord

class JSONContactBook(AbstractContactBook):
    def __init__(self):
        self.contacts = []  # Initialize an empty list to store contacts

    def save(self, filename):
        """Save contacts to a JSON file."""
        with open(filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)

    def load(self, filename):
        """Load contacts from a JSON file."""
        with open(filename, 'r') as file:
            data = json.load(file)
            for entry in data:
                self.contacts.append(ContactRecord.from_dict(entry))
