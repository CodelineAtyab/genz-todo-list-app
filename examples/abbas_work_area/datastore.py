from abc import ABC, abstractmethod


class DataStore(ABC):
    @abstractmethod
    def format(self, contact_record):
        pass