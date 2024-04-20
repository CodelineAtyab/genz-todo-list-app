"""
DataFormat is an abstract class that has three subclasses, which minuplate the data into the chosen format,
such as, TXT, JSON, CSV
"""

from abc import ABC, abstractmethod


class DataFormat(ABC):
    @abstractmethod
    def format(self, contact_record):
        pass