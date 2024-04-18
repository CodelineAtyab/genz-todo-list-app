from txt_contact_book import TXTContactBook

class AppUser:
    def __init__(self, username, file_path='contacts.txt'):
        self.username = username
        self.contact_book = TXTContactBook(file_path)

    def get_contact_book(self):
        return self.contact_book