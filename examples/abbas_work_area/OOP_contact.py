from OOP_contact_record import ContactRecord
from CSVdatastore import CSVDataStore
from TXTdatastore import TXTDataStore
from JSONdatastore import JSONDataStore
from examples.abbas_work_area.datastore import DataStore


class ContactBook:
    CONTACT_FILE_PATH = "C:/Users/71519/Documents/genz-todo-list-app/examples/abbas_work_area/data/store_contacts"

    def __init__(self, storage_format='csv'):
        self.storage_format = storage_format
        self.datastore: DataStore = None
        if storage_format == 'csv':
            self.datastore = CSVDataStore()
            self.CONTACT_FILE_PATH += ".csv"
        elif storage_format == 'txt':
            self.datastore = TXTDataStore()
            self.CONTACT_FILE_PATH += ".txt"
        elif storage_format == 'json':
            self.datastore = JSONDataStore()
            self.CONTACT_FILE_PATH += ".json"

    def open_write_file(self, data="", state="r"):
        with open(self.CONTACT_FILE_PATH, state) as contact_file:
            if state in ["a", "w"]:
                contact_file.write(data)
            elif state == "r":
                return [x.strip() for x in contact_file.readlines()]

    # chooses how to format the data based on users choice and chooses the correct class
    def format_record(self, name, contact, email, address):
        contact_record = ContactRecord(name, contact, email, address)
        # if self.storage_format == 'csv':
        #     return self.datastore.csv_format(contact_record)
        # elif self.storage_format == 'txt':
        #     return self.datastore.txt_format(contact_record)
        # elif self.storage_format == 'json':
        #     return self.datastore.json_format(contact_record)
        return self.datastore.format(contact_record)

    def store_contact(self, name, contact, email, address):
        record_str = self.format_record(name, contact, email, address)
        self.open_write_file(record_str, 'a')
        print("Contact added successfully!")
