import json

from contact_book import ContactBook, CsvContactBook, JsonContactBook
from contact_record import ContactRecord

# Dummy User Input
# list_of_user_input = [
#     ["92011497", "Atyab", "syed.atyab.hussain@gmail.com"],
#     ["92012345", "Mr.A", "mr.a@gmail.com"],
#     ["92045377", "Ms.B", "ms.b@gmail.com"],
# ]

format_of_storage = "json"

# Decide which implementation you want to use
contact_book: ContactBook = None
if format_of_storage == "csv":
    contact_book = CsvContactBook()
elif format_of_storage == "json":
    contact_book = JsonContactBook()

contact_book.load_contacts()
print(json.dumps(contact_book.contact_book_data_dict, indent=2))

# for user_input in list_of_user_input:
#     curr_contact_rec = ContactRecord(phone_number=user_input[0],
#                                      name=user_input[1],
#                                      email=user_input[2])
#
#     contact_book.store_contacts(list_of_contacts=[curr_contact_rec])

if __name__ == "__main__":
    pass
