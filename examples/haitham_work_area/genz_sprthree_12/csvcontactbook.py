import csv
from ContactBook import ContactBook
from Contact import Contact

class CSVContactBook(ContactBook):
    def load_contacts(self, filename="contacts.csv"):
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            self.contacts = [Contact(row['name'], row['phone'], row['email'], row['address']) for row in reader]

    def save_contacts(self, filename="contacts.csv"):
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['name', 'phone', 'email', 'address']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({'name': contact.name, 'phone': contact.phone, 'email': contact.email, 'address': contact.address})