from contact_book import ContactBook
from contact_record import ContactRecord
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
        existing_phone_numbers = set()

        # read existing phone numbers from the CSV file
        if os.path.exists(self.CSV_FILE_PATH):
            with open(self.CSV_FILE_PATH, "r") as csv_file:
                # skip header
                next(csv_file)
                for line in csv_file:
                    phone_number = line.split(",")[0]
                    existing_phone_numbers.add(phone_number)

        # write new contacts, skipping existing phone numbers
        with open(self.CSV_FILE_PATH, "a") as csv_file:
            for curr_contact_rec in list_of_contacts:
                phone_number = curr_contact_rec.get_phone_number()
                if phone_number not in existing_phone_numbers:
                    csv_file.write(f"{phone_number},"
                                f"{curr_contact_rec.get_name()},"
                                f"{curr_contact_rec.get_email()},"
                                f"{curr_contact_rec.get_address()}\n")
                    existing_phone_numbers.add(phone_number) 
