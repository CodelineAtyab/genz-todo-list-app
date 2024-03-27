from abc import ABC, abstractmethod
import os
import json

from contact_record import ContactRecord


class ContactBook(ABC):
    contact_book_data_dict = {}

    @abstractmethod
    def load_contacts(self):
        pass

    @abstractmethod
    def store_contacts(self, list_of_contacts):
        pass


class CsvContactBook(ContactBook):
    CSV_FILE_PATH = "./data/contact_store.csv"

    def load_contacts(self):
        loaded_records = []
        with open(self.CSV_FILE_PATH, "r") as csv_file:
            loaded_records = [rec.strip() for rec in csv_file.readlines()]

        for rec in loaded_records:
            contact_entries: list[str] = rec.split(",")
            new_contact_rec = ContactRecord(phone_number=contact_entries[0],
                                            name=contact_entries[1],
                                            email=contact_entries[2])

            # TODO: Assign the object as value
            self.contact_book_data_dict[new_contact_rec.phone_number] = {"name": new_contact_rec.name, "email": new_contact_rec.email}


    def store_contacts(self, list_of_contacts):
        file_mode = "w"
        if os.path.exists(self.CSV_FILE_PATH):
            file_mode = "a"

        with open(self.CSV_FILE_PATH, file_mode) as csv_file:
            for curr_contact_rec in list_of_contacts:
                csv_file.write(f"{curr_contact_rec.phone_number},{curr_contact_rec.name},{curr_contact_rec.email}" + "\n")


class JsonContactBook(ContactBook):
    JSON_FILE_PATH = "./data/contact_store.json"

    def load_contacts(self):
        loaded_records = []
        with open(self.JSON_FILE_PATH, "r") as json_file:
            loaded_records = [rec for rec in json_file.readlines()]

        for rec in loaded_records:
            curr_dict_rec: dict[str: dict[str: str]] = json.loads(rec)
            for curr_key in curr_dict_rec.keys():
                self.contact_book_data_dict[curr_key] = curr_dict_rec[curr_key]

    def store_contacts(self, list_of_contacts):
        dict_to_write = {}
        for curr_contact_rec in list_of_contacts:
            dict_to_write[curr_contact_rec.phone_number] = {"name": curr_contact_rec.name,
                                                            "email": curr_contact_rec.email}

        with open(self.JSON_FILE_PATH, "a") as json_file:
            json_file.write(json.dumps(dict_to_write) + "\n")
