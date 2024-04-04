from contact_book import ContactBook
from contact_record import ContactRecord
import os, json

class JsonContactBook(ContactBook):
    JSON_FILE_PATH = "./data/contact_store.json"

    def __init__(self):
        if not os.path.exists(self.JSON_FILE_PATH):
            print(f"JSON file '{self.JSON_FILE_PATH}' not found. Creating a new file...")
            self._create_empty_file()

    def _create_empty_file(self):
        with open(self.JSON_FILE_PATH, "w") as json_file:
            json.dump([], json_file)

    def load_contacts(self):
        if os.path.exists(self.JSON_FILE_PATH):
            with open(self.JSON_FILE_PATH, "r") as json_file:
                data = json.load(json_file)
                for contact_data in data:
                    phone_number = contact_data["phone_number"]
                    name = contact_data["name"]
                    email = contact_data["email"]
                    address = contact_data["address"]
                    new_contact_rec = ContactRecord(phone_number=phone_number,
                                                    name=name,
                                                    email=email,
                                                    address=address)
                    self.contact_book_data_dict[phone_number] = new_contact_rec
        else:
            print(f"JSON file '{self.JSON_FILE_PATH}' not found.")

    def store_contacts(self, list_of_contacts):
        existing_phone_numbers = set()

        # read existing phone numbers from the JSON file
        if os.path.exists(self.JSON_FILE_PATH):
            with open(self.JSON_FILE_PATH, "r") as json_file:
                data = json.load(json_file)
                existing_phone_numbers = {contact_data["phone_number"] for contact_data in data}

        # write new contacts, skipping existing phone numbers
        with open(self.JSON_FILE_PATH, "w") as json_file:
            for curr_contact_rec in list_of_contacts:
                phone_number = curr_contact_rec.get_phone_number()
                if phone_number not in existing_phone_numbers:
                    contact_data = {
                        "phone_number": phone_number,
                        "name": curr_contact_rec.get_name(),
                        "email": curr_contact_rec.get_email(),
                        "address": curr_contact_rec.get_address()
                    }
                    data.append(contact_data)
                    existing_phone_numbers.add(phone_number)

            json.dump(data, json_file, indent=4)