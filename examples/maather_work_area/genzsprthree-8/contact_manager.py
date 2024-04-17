import re
from contact_record import ContactRecord
from contact_book import CsvContactBook
from app_user import AppUser

class ContactManager:
    def __init__(self, user):
        if isinstance(user, AppUser):
            self.user = user
        else:
            raise ValueError("Invalid user provided")
        
        if isinstance(self.user.contact_book, CsvContactBook):
            self.user.contact_book.load_contacts()

    def add_contact(self, contact_data):
        new_contact = ContactRecord(
            name=contact_data["name"],
            phone_number=contact_data["phone_number"],
            email=contact_data["email"],
            address=contact_data["address"]
        )

        self.user.contact_book.contact_book_data_dict[new_contact.get_phone_number()] = new_contact

    def search_contact(self, phone_number):
        return self.user.contact_book.contact_book_data_dict.get(phone_number, None)

    def update_contact(self, phone_number, attribute, value):
        contact = self.user.contact_book.contact_book_data_dict.get(phone_number, None)
        if contact:
            if attribute == 'name':
                contact.set_name(value)
            elif attribute == 'phone_number':
                contact.set_phone_number(value)
            elif attribute == 'email':
                contact.set_email(value)
            elif attribute == 'address':
                contact.set_address(value)
            else:
                print("Invalid attribute.")
        else:
            print("Contact not found.")

    def delete_contact(self, phone_number):
        if phone_number in self.user.contact_book.contact_book_data_dict:
            del self.user.contact_book.contact_book_data_dict[phone_number]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    def validate_email(email):
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return bool(email_pattern.match(email))