from CSVContactBook import CSVContactBook

class AppUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.contact_book = CSVContactBook()