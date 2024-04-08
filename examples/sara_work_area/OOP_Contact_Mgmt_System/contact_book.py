from abc import ABC, abstractmethod
from contact_record import ContactRecord


class ContactBook(ABC):
    contact_book_data_dict = {}

    @abstractmethod
    def load_contacts(self):
        pass

    @abstractmethod
    def store_contact(self, contact: ContactRecord):
        pass

    @abstractmethod
    def update_contact(self, phone_number: str, updated_contact: ContactRecord):
        pass

    @abstractmethod
    def delete_contact(self, phone_number: str):
        pass

    @abstractmethod
    def return_formatted_contacts(self):
        pass
