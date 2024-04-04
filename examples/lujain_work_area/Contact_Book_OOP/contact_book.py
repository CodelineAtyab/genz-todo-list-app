# contact_book.py

from abc import ABC, abstractmethod
from contact_record import ContactRecord

class AbstractContactBook(ABC):
    @abstractmethod
    def save(self, filename):
        """Save the contact book to a file."""
        pass

    @abstractmethod
    def load(self, filename):
        """Load the contact book from a file."""
        pass

    def add_contact(self, contact):
        """Add a contact to the contact book."""
        self.contacts.append(contact)

    def delete_contact(self, identifier):
        """Delete a contact from the contact book."""
        self.contacts = [contact for contact in self.contacts if not any(contact.__dict__[key] == identifier for key in contact.__dict__)]

    def update_contact(self, identifier, new_contact):
        """Update a contact in the contact book."""
        for contact in self.contacts:
            if any(contact.__dict__[key] == identifier for key in contact.__dict__):
                for key, value in new_contact.items():
                    setattr(contact, key, value)

    def search_contact(self, identifier):
        """Search for a contact in the contact book."""
        return [contact for contact in self.contacts if any(contact.__dict__[key] == identifier for key in contact.__dict__)]

from json_contact_book import JSONContactBook  # Importing JSONContactBook class
from csv_contact_book import CSVContactBook  # Importing CSVContactBook class
