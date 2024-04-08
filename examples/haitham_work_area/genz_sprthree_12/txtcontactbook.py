from ContactBook import ContactBook
from Contact import Contact

class TXTContactBook(ContactBook):
    def load_contacts(self, filename="contacts.txt"):
        with open(filename, 'r') as file:
            self.contacts = [Contact(*line.strip().split(", ")) for line in file]

    def save_contacts(self, filename="contacts.txt"):
        with open(filename, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact.name}, {contact.phone}, {contact.email}, {contact.address}\n")