from abc import ABC, abstractmethod

class ContactBook(ABC):
    @abstractmethod
    def add_contact(self, contact):
        pass

    @abstractmethod
    def delete_contact(self, name):
        pass

    @abstractmethod
    def update_contact(self, old_name, **kwargs):
        pass

    @abstractmethod
    def list_contacts(self):
        pass

    @abstractmethod
    def save_contacts(self):
        pass

    @abstractmethod
    def load_contacts(self):
        pass

    @abstractmethod
    def download_contacts(self, format_type):
        pass
