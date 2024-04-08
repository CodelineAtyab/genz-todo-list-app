from CSVContactBook import CSVContactBook
from JSONContactBook import JSONContactBook
from TXTContactBook import TXTContactBook


class AppUser:
    def __init__(self, username, email, format='csv'):
        self.username = username
        self.email = email
        if format == 'csv':
            self.contact_book = CSVContactBook()
        elif format == 'json':
            self.contact_book = JSONContactBook()
        elif format == 'txt':
            self.contact_book = TXTContactBook()
        else:
            raise
