from contact_book import CsvContactBook, JsonContactBook
from contact_record import ContactRecord

# Dummy User Input
list_of_user_input = [
    ["92011497", "Atyab", "syed.atyab.hussain@gmail.com"],
    ["92012345", "Mr.A", "mr.a@gmail.com"],
    ["92045377", "Ms.B", "ms.b@gmail.com"],
]

format_of_storage = "csv"

# Decide which implementation you want to use
contact_book = None
if format_of_storage == "csv":
    contact_book = CsvContactBook()
elif format_of_storage == "json":
    contact_book = JsonContactBook()

for user_input in list_of_user_input:
    curr_contact_rec = ContactRecord(phone_number=user_input[0],
                                     name=user_input[1],
                                     email=user_input[2])

    contact_book.store_contacts(list_of_contacts=[curr_contact_rec])

if __name__ == "__main__":
    pass
