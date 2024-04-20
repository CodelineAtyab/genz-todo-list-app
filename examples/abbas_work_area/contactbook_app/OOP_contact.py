import json
import os
from OOP_contact_record import ContactRecord
from CSVdataformat import CSVDataFormat
from TXTdataformat import TXTDataFormat
from JSONdataformat import JSONDataFormat
from examples.abbas_work_area.dataformat import DataFormat


class ContactBook:
    BASE_FILE_PATH = "./data/store_contacts"

    def __init__(self, storage_format='csv'):
        self.set_datastore(storage_format)
        self.storage_format = storage_format
        self.dataformat: DataFormat = CSVDataFormat()
        self.CONTACT_FILE_PATH = f"{self.BASE_FILE_PATH}.{storage_format}"

    def set_datastore(self, storage_format):
        if storage_format == 'csv':
            self.dataformat = CSVDataFormat()
        elif storage_format == 'txt':
            self.dataformat = TXTDataFormat()
        elif storage_format == 'json':
            self.dataformat = JSONDataFormat()
        self.CONTACT_FILE_PATH = f"{self.BASE_FILE_PATH}.{storage_format}"

    def write_heading(self):
        self.open_write_file("Name,Contact,Email,Address\n", 'w')  # writes heading of csv

    def if_header_exists(self):
        if not os.path.exists(self.CONTACT_FILE_PATH):  # checks if file exists
            self.write_heading()

    def open_write_file(self, data="", state="r"):
        """
        contains all file related functions such as, Write, Read, Append to main file
        :param data: user inputted record
        :param state: a, r, or w
        :return: Data Saved Successfully!
        """
        with open(self.CONTACT_FILE_PATH, state) as contact_file:
            if state in ["a", "w"]:
                contact_file.write(data)
            elif state == "r":
                return [x.strip() for x in contact_file.readlines()]

    # chooses how to format the data based on users choice and chooses the correct class
    def format_record(self, name, contact, email, address):
        """
        :param name: name
        :param contact: phone number
        :param email: email
        :param address: address
        :return: chooses the format of file based on user input
        """
        contact_record = ContactRecord(name, contact, email, address)
        return self.dataformat.format(contact_record)

    def store_contact(self, name, contact, email, address):
        contact_record = ContactRecord(name, contact, email, address)
        store = CSVDataFormat()
        record_str = store.format(contact_record)
        self.open_write_file(record_str, 'a')
        print("Contact added successfully!")

    def load_contacts(self, new_format):
        """
        :param new_format: contains users chosen format e.g: csv, txt, json
        :return: stores formatted data into the chosen file type in order to execute users request to
                 download data in chosen file format.
        """
        existing_contacts = self.open_write_file()
        self.set_datastore(new_format)
        self.open_write_file(data="", state='w')
        for contact in existing_contacts[1:]:
            name, contact, email, address = contact.split(",")
            record_str = self.format_record(name.strip(), contact.strip(), email.strip(), address.strip())
            self.open_write_file(record_str, 'a')

        print(f"All contacts have been converted and stored in {new_format} format.")

    def read_contact(self, search):
        """
        Search for a specific record based on unique key, in this case the name.
        e.g: input: John Doe
             output: Name: John Doe, Phone Number: 1234, Email: John@gmail.com, Address: Oman
        """
        try:
            contacts = self.open_write_file()
            for contact in contacts[1:]:
                contact_details = contact.split(",")

                if contact_details[1].strip().lower() == search.strip().lower():
                    return f"[Name: {contact_details[0]}, Phone Number: {contact_details[1]}, Email: {contact_details[2]}, Address: {contact_details[3]}]"
            return "Not found"
        except Exception as ex:
            print("Error", ex)

    def delete_contact(self, incoming):
        """
            Deletes existing results based on name
            input: Abbas
            output: Deleted Successfully!
        """
        result_to_del = self.read_contact(incoming)
        result_split = result_to_del.split(",")
        all_lines = self.open_write_file("", 'r')
        result = []

        try:
            for contact in all_lines[1:]:
                contact_details = contact.split(",")
                if contact_details[1] not in result_split[1]:
                    result.append(contact + '\n')
            self.write_heading()
            for contact in result:
                self.open_write_file(contact, 'a')

            print("Record Deleted Successfully!")

        except Exception as ex:
            print("Error", ex)

    def update_contact(self, old_info, name, contact, email, address):
        """
            Updates existing results based on name
            input: Abbas
            output: Updated Successfully!
        """
        updated_line = self.read_contact(old_info)
        updated = updated_line.split(',')
        all_lines = self.open_write_file("", 'r')
        result = []

        try:
            for contacts in all_lines[1:]:
                contact_details = contacts.split(",")
                if contact_details[1] not in updated[1]:
                    result.append(contacts)
                elif contact_details[1] in updated[1]:
                    result.append(f"{name}, {contact}, {email}, {address}")

            self.write_heading()

            for contacts in result:
                self.open_write_file(contacts + '\n', 'a')
            print("Updated Successfully!")
        except Exception as ex:
            print("Error", ex)


