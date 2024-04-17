from abc import ABC, abstractmethod
from contact_record import ContactRecord

class AbstractContactBook(ABC):
    @abstractmethod
    def save(self, filename, format):
        """Save the contact book to a file."""
        pass

    @abstractmethod
    def load(self, filename, format):
        """Load the contact book from a file."""
        pass

    def get_file_extension(self, format):
        """Get the file extension based on the format."""
        if format == 'csv':
            return '.csv'
        elif format == 'json':
            return '.json'
        else:
            raise ValueError("Unsupported file format")

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """Add a contact to the contact book."""
        self.contacts.append(contact)

    def delete_contact(self, identifier):
        """Delete a contact from the contact book."""
        self.contacts = [contact for contact in self.contacts if
                         not any(contact.__dict__[key] == identifier for key in contact.__dict__)]

    def update_contact(self, identifier, new_contact):
        """Update a contact in the contact book."""
        for contact in self.contacts:
            if any(contact.__dict__[key] == identifier for key in contact.__dict__):
                for key, value in new_contact.items():
                    setattr(contact, key, value)

    def search_contact(self, identifier):
        """Search for a contact in the contact book."""
        return [contact for contact in self.contacts if
                any(contact.__dict__[key] == identifier for key in contact.__dict__)]

    def save(self, filename, format):
        """Save the contact book to a file."""
        # Implementation for saving to file based on format
        pass

    def load(self, filename, format):
        """Load the contact book from a file."""
        # Implementation for loading from file based on format
        pass

    def get_file_extension(self, format):
        """Get the file extension based on the format."""
        if format == 'csv':
            return '.csv'
        elif format == 'json':
            return '.json'
        else:
            raise ValueError("Unsupported file format")
