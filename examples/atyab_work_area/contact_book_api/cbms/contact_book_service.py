import json
from cbms.contact_record import ContactRecord
from cbms.contact_book import ContactBook


contact_book = ContactBook()


lines_in_file = []
with open("./cbms/data/data_store.json") as data_file:
    lines_in_file = data_file.readlines()

list_of_contact_records = []
for line in lines_in_file:
    curr_rec_dict: dict[str, str] = json.loads(line.strip())
    curr_contact_rec = ContactRecord(phone_number=curr_rec_dict["phone_no"],
                                     name=curr_rec_dict["name"],
                                     email=curr_rec_dict["email"])
    list_of_contact_records.append(curr_contact_rec)

contact_book.contact_records = list_of_contact_records
