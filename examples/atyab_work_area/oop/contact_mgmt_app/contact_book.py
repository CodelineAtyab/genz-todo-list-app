from abc import ABC
import os
import json


class ContactBook(ABC):
    def load_contacts(self) -> list[str]:
        print("Loaded Contacts Successfully!")

    def store_contacts(self, list_of_contacts):
        for curr_contact_rec in list_of_contacts:
            print(curr_contact_rec)


class CsvContactBook(ContactBook):
    CSV_FILE_PATH = "./data/contact_store.csv"

    def store_contacts(self, list_of_contacts):
        file_mode = "w"
        if os.path.exists(self.CSV_FILE_PATH):
            file_mode = "a"

        with open(self.CSV_FILE_PATH, file_mode) as csv_file:
            for curr_contact_rec in list_of_contacts:
                csv_file.write(f"{curr_contact_rec.phone_number},{curr_contact_rec.name},{curr_contact_rec.email}" + "\n")


class JsonContactBook(ContactBook):
    JSON_FILE_PATH = "./data/contact_store.json"

    def store_contacts(self, list_of_contacts):
        dict_to_write = {}
        for curr_contact_rec in list_of_contacts:
            dict_to_write[curr_contact_rec.phone_number] = {"name": curr_contact_rec.name,
                                                            "email": curr_contact_rec.email}

        with open(self.JSON_FILE_PATH, "a") as json_file:
            json_file.write(json.dumps(dict_to_write) + "\n")
