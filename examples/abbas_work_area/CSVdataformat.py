from examples.abbas_work_area.dataformat import DataFormat


class CSVDataFormat(DataFormat):
    def format(self, contact_record):
        return f"{contact_record.add_name}, {contact_record.add_contact}, {contact_record.add_email}, {contact_record.add_address}\n"

