# contact_book.py

from contact_records import ContactRecords

class ContactBook:
    def __init__(self, csv_file):
        self.contact_records = ContactRecords(csv_file)

    def add_contact(self, name, phone, email, address):
        contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
        self.contact_records.add_contact(contact)

    def delete_contact(self, identifier):
        self.contact_records.delete_contact(identifier)

    def update_contact(self, identifier, new_phone=None, new_email=None, new_address=None):
        new_contact = {}
        if new_phone:
            new_contact['Phone'] = new_phone
        if new_email:
            new_contact['Email'] = new_email
        if new_address:
            new_contact['Address'] = new_address
        self.contact_records.update_contact(identifier, new_contact)

    def search_contact(self, identifier):
        return self.contact_records.search_contact(identifier)
