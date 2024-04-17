from contact_book import CsvContactBook

class AppUser:
    def __init__(self, username, email, contact_book=None):
        self.username = username
        self.email = email
        if contact_book is None:
            contact_book = CsvContactBook()
        self.contact_book = contact_book

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_contact_book(self):
        return self.contact_book

    def set_contact_book(self, contact_book):
        self.contact_book = contact_book

