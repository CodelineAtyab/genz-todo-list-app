from examples.abbas_work_area.datastore import DataStore


class TXTDataStore(DataStore):
    def format(self, contact_record):
        return f"Name: {contact_record.add_name}, Contact: {contact_record.add_contact}, Email: {contact_record.add_email}, Address: {contact_record.add_address}\n"
