from abc import ABC, abstractmethod


class ContactBook(ABC):
    def __init__(self):
        self.contacts = []

    @abstractmethod
    def load_contacts(self, filename):
        pass

    @abstractmethod
    def save_contacts(self, filename):
        pass
