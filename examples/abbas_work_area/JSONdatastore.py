import json

from examples.abbas_work_area.datastore import DataStore


class JSONDataStore(DataStore):
    def format(self, contact_record):
        return json.dumps({
            "name": contact_record.add_name,
            "contact": contact_record.add_contact,
            "email": contact_record.add_email,
            "address": contact_record.add_address
        }) + "\n"

