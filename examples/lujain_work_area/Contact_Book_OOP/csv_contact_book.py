# csv_contact_book.py

import csv
from contact_book import AbstractContactBook
from contact_record import ContactRecord

class CSVContactBook(AbstractContactBook):
    def __init__(self):
        self.contacts = []  # Initialize an empty list to store contacts

    def save(self, filename, format):
        """Save contacts to a CSV file."""
        file_extension = self.get_file_extension(format)
        with open(filename + file_extension, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Phone', 'Email', 'Address'])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())

    def load(self, filename, format):
        """Load contacts from a CSV file."""
        file_extension = self.get_file_extension(format)
        with open(filename + file_extension, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.contacts.append(ContactRecord.from_dict(row))

    def load(self, filename, format):
        """Load contacts from a CSV file."""
        file_extension = self.get_file_extension(format)
        with open(filename + file_extension, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.contacts.append(ContactRecord.from_dict(row))

