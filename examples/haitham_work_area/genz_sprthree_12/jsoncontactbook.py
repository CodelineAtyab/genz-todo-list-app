import json
from ContactBook import ContactBook
from Contact import Contact


class JSONContactBook(ContactBook):
    def load_contacts(self, filename="contacts.json"):
        with open(filename, 'r') as file:
            contacts_list = json.load(file)
            self.contacts = [Contact(**contact) for contact in contacts_list]

    def save_contacts(self, filename="contacts.json"):
        with open(filename, 'w') as file:
            json.dump([contact.__dict__ for contact in self.contacts], file, indent=4)