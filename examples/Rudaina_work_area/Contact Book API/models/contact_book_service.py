from contact_book import ContactBook
from contact_record import ContactRecord


class ContactBookService:
    def __init__(self):
        self.contact_book = ContactBook()

    def add_contact(self, name, phone, email, address):
        contact = ContactRecord(name, phone, email, address)
        self.contact_book.add(contact)

    def search_contact(self, email):
        return self.contact_book.search(email)

    def update_contact(self, email, updated_contact):
        return self.contact_book.update(email, updated_contact)

    def delete_contact(self, email):
        return self.contact_book.delete(email)
