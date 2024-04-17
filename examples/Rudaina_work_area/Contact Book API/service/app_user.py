from contact_book import JsonContactBook
from contact_record import ContactRecord


class AppUser:
    user_contact_books = {}  # Dictionary to store user email and associated ContactBook

    def __init__(self, name, email, phone, contact=None):
        self.__name = name
        self.__email = email
        self.__phone = phone

        # Instantiate a concrete subclass of ContactBook, such as JsonContactBook
        if email in AppUser.user_contact_books:
            # Use existing ContactBook if the user already exists
            self.contact_book = AppUser.user_contact_books[email]
        else:
            # If user does not exist, create a new JSON file and ContactBook
            self.contact_book = JsonContactBook(self, email)
            AppUser.user_contact_books[email] = self.contact_book

            # Create a contact for the user if provided
            if contact:
                self.contact_book.add(contact)
            else:
                self_contact = ContactRecord(name, email, phone, "Address: Not specified")
                self.contact_book.add(self_contact)

            self.contact_book.save_contact()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone
