from contact_book import ContactBook
from contact import ContactRecord
import csv
import json


class TXTContactBook(ContactBook):
    def __init__(self, file_path):
        self.file_path = file_path
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file_path, 'r') as file:
                self.contacts = [ContactRecord(*line.strip().split(', ')) for line in file.readlines()]
            print("Contacts loaded from TXT.")
        except FileNotFoundError:
            print("File not found, starting with an empty contact book.")

    def save_contacts(self):
        with open(self.file_path, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact.name}, {contact.phone_number}, {contact.email}, {contact.address}\n")
        print("Contacts saved to TXT.")

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        self.save_contacts()

    def update_contact(self, old_name, **kwargs):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.__dict__.update((k, v) for k, v in kwargs.items() if v is not None)
        self.save_contacts()

    def list_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts to display.")

    def download_contacts(self, format_type):
        if format_type == 'CSV':
            with open('contacts.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Phone Number', 'Email', 'Address'])
                for contact in self.contacts:
                    writer.writerow([contact.name, contact.phone_number, contact.email, contact.address])
            print("Contacts downloaded as CSV.")
        elif format_type == 'JSON':
            with open('contacts.json', 'w') as file:
                json.dump([contact.__dict__ for contact in self.contacts], file, indent=4)
            print("Contacts downloaded as JSON.")
        elif format_type == 'TXT':
            self.save_contacts()  # Re-use the existing save functionality
            print("Contacts downloaded as TXT.")