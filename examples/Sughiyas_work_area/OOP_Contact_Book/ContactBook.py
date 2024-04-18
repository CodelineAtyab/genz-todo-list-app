import csv
import json
from ContactRecord import ContactRecord
from AbstractConactBook import AbstractContactBook


class ContactBook(AbstractContactBook):
    def save_to_file(self, file_path):
        extension = file_path.split('.')[-1]
        if extension == 'csv':
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Name', 'Phone', 'Email', 'Address'])
                for contact in self.contacts:
                    writer.writerow([contact.name, contact.phone, contact.email, contact.address])
        elif extension == 'json':
            with open(file_path, 'w') as jsonfile:
                json.dump([vars(contact) for contact in self.contacts], jsonfile, indent=4)
        elif extension == 'txt':
            with open(file_path, 'w') as txtfile:
                for contact in self.contacts:
                    txtfile.write(f"{contact.name}, {contact.phone}, {contact.email}, {contact.address}\n")
        else:
            print("Unsupported file format. please select csv, json or txt")

    def load_from_file(self, file_path):
        extension = file_path.split('.')[-1]
        if extension == 'csv':
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    contact = ContactRecord(row['Name'], row['Phone'], row['Email'], row['Address'])
                    self.add_contact(contact)
        elif extension == 'json':
            with open(file_path, 'r') as jsonfile:
                data = json.load(jsonfile)
                for item in data:
                    contact = ContactRecord(**item)
                    self.add_contact(contact)
        elif extension == 'txt':
            with open(file_path, 'r') as txtfile:
                for line in txtfile:
                    name, phone, email, address = line.strip().split(', ')
                    contact = ContactRecord(name, phone, email, address)
                    self.add_contact(contact)
        else:
            print("Unsupported file format. please select csv, json or txt")
