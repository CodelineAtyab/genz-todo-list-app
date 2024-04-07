import csv
from abc import ABC, abstractmethod
import os
import json

from contact_record import ContactRecord

class AppUser:
    def __init__(self, username, email, storage_format='json'):
        self.username = username
        self.email = email
        if storage_format == 'json':
            self.contact_book = JsonContactBook()
        elif storage_format == 'csv':
            self.contact_book = CsvContactBook()
        elif storage_format == 'txt':
            self.contact_book = TextContactBook()
        else:
            raise ValueError(f"Unsupported storage format: {storage_format}")

    def get_contact_book(self):
        return self.contact_book


class ContactBook(ABC):
    def __init__(self):
        self.contacts = []

    @abstractmethod
    def load_contacts(self, file_path):
        pass

    @abstractmethod
    def save_contacts(self, file_path):
        pass

    def add_contact(self, contact_record):
        self.contacts.append(contact_record)

    def delete_contact(self, contact_record):
        self.contacts.remove(contact_record)

    def find_contact(self, name):
        return [contact for contact in self.contacts if contact.name == name]


class JsonContactBook(ContactBook):
    def load_contacts(self, file_path):
        with open(file_path, 'r') as file:
            self.contacts = json.load(file)

    def save_contacts(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.contacts, file, default=lambda o: o.__dict__, indent=4)

class CsvContactBook(ContactBook):
    def load_contacts(self, file_path):
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            self.contacts = [ContactRecord(**row) for row in reader]

    def save_contacts(self, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'phone_number', 'email', 'address'])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.__dict__)

class TextContactBook(ContactBook):
    def load_contacts(self, file_path):
        self.contacts = []
        with open(file_path, 'r') as file:
            contact_data = file.read().strip().split('\n\n')  # Split contacts by blank line
            for entry in contact_data:
                lines = entry.split('\n')  # Split each contact's data by newline
                contact_dict = {}
                for line in lines:
                    key, value = line.split(': ', 1)  # Assuming each line is in the format "key: value"
                    contact_dict[key.strip()] = value.strip()
                self.contacts.append(ContactRecord(**contact_dict))

    def save_contacts(self, file_path):
        with open(file_path, 'w') as file:
            for contact in self.contacts:
                file.write(f"name: {contact.name}\n")
                file.write(f"phone_number: {contact.phone_number}\n")
                file.write(f"email: {contact.email}\n")
                file.write(f"address: {contact.address}\n\n")  # Double newline to separate contacts



"""class ContactBook(ABC):
    contact_book_data_dict = {}

    @abstractmethod
    def load_contacts(self):
        pass

    @abstractmethod
    def store_contacts(self, list_of_contacts):
        pass"""


"""class CsvContactBook(ContactBook):
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
        try:
            with open(self.JSON_FILE_PATH, "r") as json_file:
                self.contact_book_data_dict = json.load(json_file)
        except FileNotFoundError:
            print("JSON file not found. Starting with an empty contact book.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty contact book.")

    def store_contacts(self, list_of_contacts):
        for curr_contact_rec in list_of_contacts:
            self.contact_book_data_dict[curr_contact_rec.get_phone_number()] = {
                "name": curr_contact_rec.name,
                "email": curr_contact_rec.email
            }
        with open(self.JSON_FILE_PATH, "w") as json_file:
            json.dump(self.contact_book_data_dict, json_file, indent=4)
"""
"""class JsonContactBook(ContactBook):
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
            json_file.write(json.dumps(dict_to_write) + "\n")"""
