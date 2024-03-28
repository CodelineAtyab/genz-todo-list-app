# contact_records.py

import csv
import os

class ContactRecords:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fieldnames = ['Name', 'Phone', 'Email', 'Address']
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if not os.path.exists(self.csv_file):
            return []
        with open(self.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def save_contacts(self):
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.contacts)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def delete_contact(self, identifier):
        self.contacts = [contact for contact in self.contacts if contact['Name'] != identifier and
                         contact['Email'] != identifier and contact['Phone'] != identifier]
        self.save_contacts()

    def update_contact(self, identifier, new_contact):
        for contact in self.contacts:
            if contact['Name'] == identifier or contact['Email'] == identifier or contact['Phone'] == identifier:
                contact.update(new_contact)
        self.save_contacts()

    def search_contact(self, identifier):
        results = []
        for contact in self.contacts:
            if contact['Name'] == identifier or contact['Email'] == identifier or contact['Phone'] == identifier:
                results.append(contact)
        return results

    
