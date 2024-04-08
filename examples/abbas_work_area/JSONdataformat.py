import json

from examples.abbas_work_area.dataformat import DataFormat


class JSONDataFormat(DataFormat):
    def format(self, contact_record):
        return json.dumps({
            "name": contact_record.add_name,
            "contact": contact_record.add_contact,
            "email": contact_record.add_email,
            "address": contact_record.add_address
        }) + "\n"

