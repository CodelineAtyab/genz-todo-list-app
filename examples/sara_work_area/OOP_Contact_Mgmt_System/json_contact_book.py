from contact_book import ContactBook
from contact_record import ContactRecord
import json
import os


class JsonContactBook(ContactBook):

    def __init__(self, phone_number: str):
        self.JSON_FILE_PATH = f"./data/{phone_number}_contacts.json"
        if not os.path.exists(self.JSON_FILE_PATH):
            with open(f"./data/{phone_number}_contacts.json", "w") as json_file:
                json.dump([], json_file)

    def load_contacts(self):
        try:
            with open(self.JSON_FILE_PATH, "r") as contact_file:
                loaded_data = json.load(contact_file)
                for contact_info in loaded_data:
                    new_contact_rec = ContactRecord(phone_number=contact_info.get("phone_number"),
                                                    name=contact_info.get("name"),
                                                    email=contact_info.get("email"),
                                                    address=contact_info.get("address"))

                    self.contact_book_data_dict[new_contact_rec.get_phone_number()] = {"name": new_contact_rec.get_name(),
                                                                                       "email": new_contact_rec.get_email(),
                                                                                       "address": new_contact_rec.get_address()}
        except json.decoder.JSONDecodeError:
            print("The file is empty or does not contain valid JSON data.")

    def store_contact(self, contact: ContactRecord):
        with open(self.JSON_FILE_PATH, "r") as json_file:
            contacts = json.load(json_file)

        phone_exists = False
        if contact.get_phone_number() in self.contact_book_data_dict:
            print(f"\nContact with phone number {contact.get_phone_number()} already exists.\n")
            phone_exists = True
        if not phone_exists:
            contact_dict = {
                "name": contact.get_name(),
                "phone_number": contact.get_phone_number(),
                "email": contact.get_email(),
                "address": contact.get_address()
            }
            contacts.append(contact_dict)
            with open(self.JSON_FILE_PATH, "w") as json_file:
                json.dump(contacts, json_file, indent=2)
            print("\nContact added successfully.\n")
            self.contact_book_data_dict[contact.get_phone_number()] = {"name": contact.get_name(),
                                                                       "email": contact.get_email(),
                                                                       "address": contact.get_address()}

    def update_contact(self, phone_number: str, updated_contact: ContactRecord):
        with open(self.JSON_FILE_PATH, "r+") as contact_file:
            loaded_data = json.load(contact_file)
            for index, json_object in enumerate(loaded_data):
                if phone_number == json_object["phone_number"]:
                    loaded_data[index] = {"name": updated_contact.get_name(),
                                          "phone_number": updated_contact.get_phone_number(),
                                          "email": updated_contact.get_email(),
                                          "address": updated_contact.get_address()}
                    break
            contact_file.seek(0)
            contact_file.truncate()
            json.dump(loaded_data, contact_file, indent=2)
            self.contact_book_data_dict.pop(phone_number, None)
            self.contact_book_data_dict[updated_contact.get_phone_number()] = {"name": updated_contact.get_name(),
                                                                               "email": updated_contact.get_email(),
                                                                               "address": updated_contact.get_address()}
        print("\nContact updated successfully.\n")

    def delete_contact(self, phone_number: str):
        contact_deleted = False
        with open(self.JSON_FILE_PATH, "r+") as contact_file:
            loaded_data = json.load(contact_file)
            contact_file.seek(0)
            contact_file.truncate()
            remaining_contacts = []
            for json_object in loaded_data:
                if json_object["phone_number"] == phone_number:
                    contact_deleted = True
                else:
                    remaining_contacts.append(json_object)
            json.dump(remaining_contacts, contact_file, indent=2)

        if contact_deleted:
            self.contact_book_data_dict.pop(phone_number, None)
            print("\nContact deleted successfully.\n")
        else:
            print(f"The contact with the specified number {phone_number} does not exist.")

    import json

    import json

    def return_formatted_contacts(self):
        formatted_contacts = []
        with open(self.JSON_FILE_PATH, "r") as contact_file:
            contacts_data = json.load(contact_file)
            for contact in contacts_data:
                formatted_contact = {key: str(value) for key, value in contact.items()}
                formatted_contacts.append(formatted_contact)

        formatted_json = json.dumps(formatted_contacts)
        # print(formatted_contacts)
        return formatted_json

