from contact_book import ContactBook
from contact_record import ContactRecord
import os


class CsvContactBook(ContactBook):

    def __init__(self, phone_number: str):
        # open(f"./data/{phone_number}_contacts.csv", "w")
        self.CSV_FILE_PATH = f"./data/{phone_number}_contacts.csv"
        open(self.CSV_FILE_PATH, "r+") if os.path.exists(self.CSV_FILE_PATH) else open(self.CSV_FILE_PATH, "w")

    def load_contacts(self):
        with open(self.CSV_FILE_PATH, "r") as contact_file:
            for line in contact_file:
                contact_info = line.strip().split(",")
                new_contact_rec = ContactRecord(phone_number=contact_info[1],
                                                name=contact_info[0],
                                                email=contact_info[2],
                                                address=contact_info[3])
                self.contact_book_data_dict[new_contact_rec.get_phone_number()] = {"name": new_contact_rec.get_name(),
                                                                                   "email": new_contact_rec.get_email(),
                                                                                   "address": new_contact_rec.get_address()}

    def store_contact(self, contact: ContactRecord):
        phone_exists = False
        if contact.get_phone_number() in self.contact_book_data_dict:
            print(f"\nContact with phone number {contact.get_phone_number()} already exists.\n")
            phone_exists = True

        if not phone_exists:
            with open(self.CSV_FILE_PATH, "a") as contact_file:
                contact_file.write(
                    f"{contact.get_name()},{contact.get_phone_number()},{contact.get_email()},{contact.get_address()},\n")
                print("\nContact added successfully.\n")
            self.contact_book_data_dict[contact.get_phone_number()] = {"name": contact.get_name(),
                                                                       "email": contact.get_email(),
                                                                       "address": contact.get_address()}

    def update_contact(self, phone_number: str, updated_contact: ContactRecord):
        with (open(self.CSV_FILE_PATH, "r+") as contact_file):
            lines = contact_file.readlines()
            for index, line in enumerate(lines):
                contact_info = line.strip().split(",")
                if phone_number == contact_info[1]:
                    lines[index] = updated_contact.get_name() + "," + updated_contact.get_phone_number() + "," + str(updated_contact.set_email(updated_contact.get_email())) + "," + updated_contact.get_address() + "," + "\n"
                    break
            contact_file.seek(0)
            contact_file.writelines(lines)
            contact_file.truncate()
            self.contact_book_data_dict.pop(phone_number)
            self.contact_book_data_dict[updated_contact.get_phone_number()] = {"name": updated_contact.get_name(),
                                                                               "email": updated_contact.get_email(),
                                                                               "address": updated_contact.get_address()}
            print("\nContact updated successfully.\n")

    def delete_contact(self, phone_number: str):
        contact_deleted = False
        with open(self.CSV_FILE_PATH, "r+") as contact_file:
            lines = contact_file.readlines()
            contact_file.seek(0)
            for line in lines:
                contact_info = line.strip().split(",")
                if contact_info[1] == phone_number:
                    self.contact_book_data_dict.pop(phone_number)
                    print(f"\nContact deleted successfully\n")
                    contact_deleted = True
                else:
                    contact_file.write(line)
            contact_file.truncate()

        if not contact_deleted:
            print(f"The contact with the specified number {phone_number} does not exist")

    def return_formatted_contacts(self):
        formatted_lines = []
        with open(self.CSV_FILE_PATH, "r") as contact_file:
            for line in contact_file:
                contact_info = [item.strip() for item in line.strip().split(",") if item.strip()]
                if contact_info:  # Check if the resulting list is not empty
                    formatted_line = ','.join(contact_info)
                    formatted_lines.append(formatted_line)
            # print('\n'.join(formatted_lines))
        return '\n'.join(formatted_lines)

