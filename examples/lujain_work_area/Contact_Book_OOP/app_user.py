# app_user.py

from contact_book import ContactBook

class AppUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.contact_book = ContactBook()

    def add_contact(self, contact):
        """Add a contact to the user's ContactBook."""
        self.contact_book.add_contact(contact)

    def delete_contact(self, identifier):
        """Delete a contact from the user's ContactBook."""
        self.contact_book.delete_contact(identifier)

    def update_contact(self, identifier, new_contact):
        """Update a contact in the user's ContactBook."""
        self.contact_book.update_contact(identifier, new_contact)

    def search_contact(self, identifier):
        """Search for a contact in the user's ContactBook."""
        return self.contact_book.search_contact(identifier)

    def save_contact_book(self, filename, format):
        """Save the user's ContactBook to a file."""
        if format == 'csv':
            self.contact_book.save_to_csv(filename)
        elif format == 'json':
            self.contact_book.save_to_json(filename)

    def load_contact_book(self, filename, format):
        """Load the user's ContactBook from a file."""
        if format == 'csv':
            self.contact_book.load_from_csv(filename)
        elif format == 'json':
            self.contact_book.load_from_json(filename)
