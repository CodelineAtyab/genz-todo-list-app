from examples.abbas_work_area.dataformat import DataFormat


class TXTDataFormat(DataFormat):
    def format(self, contact_record):
        return f"Name: {contact_record.add_name}, Contact: {contact_record.add_contact}, Email: {contact_record.add_email}, Address: {contact_record.add_address}\n"
