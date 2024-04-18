from abc import ABC, abstractmethod
from contact_record import ContactRecord

class ContactBook(ABC):
    contact_book_data_dict = {}

    @abstractmethod
    def load_contacts(self):
        pass

    @abstractmethod
    def store_contacts(self, list_of_contacts):
        pass


        