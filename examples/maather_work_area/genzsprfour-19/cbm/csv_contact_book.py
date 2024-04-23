from cbm.contact_book import ContactBook
from cbm.contact_record import ContactRecord
import os

class CsvContactBook(ContactBook):
    CSV_FILE_PATH = "./data/contact_store.csv"

    def __init__(self):
        if not os.path.exists(self.CSV_FILE_PATH):
            print(f"CSV file '{self.CSV_FILE_PATH}' not found. Creating a new file...")
            os.makedirs(os.path.dirname(self.CSV_FILE_PATH), exist_ok=True)  
            header = "phone number,name,email,address"
            with open(self.CSV_FILE_PATH, "w") as file:
                file.write(header + "\n")

    def load_contacts(self):
        if os.path.exists(self.CSV_FILE_PATH):
            loaded_records = []
            with open(self.CSV_FILE_PATH, "r") as csv_file:
                loaded_records = [rec.strip() for rec in csv_file.readlines()]

            for rec in loaded_records[1:]:
                contact_entries = rec.split(",")
                # create ContactRecord and add it to contact book data
                new_contact_rec = ContactRecord(phone_number=contact_entries[0],
                                                name=contact_entries[1],
                                                email=contact_entries[2],
                                                address=contact_entries[3])
                self.contact_book_data_dict[new_contact_rec.get_phone_number()] = new_contact_rec

    def store_contacts(self, list_of_contacts):
        with open(self.CSV_FILE_PATH, "w") as csv_file:
            csv_file.write("phone_number,name,email,address\n")  # Write header
            for curr_contact_rec in list_of_contacts:
                phone_number = curr_contact_rec.get_phone_number()
                name = curr_contact_rec.get_name()
                email = curr_contact_rec.get_email()
                address = curr_contact_rec.get_address()
                csv_file.write(f"{phone_number},{name},{email},{address}\n")
