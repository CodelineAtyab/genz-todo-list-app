from OOP_contact_record import ContactRecord
from OOP_contact import ContactBook

contact_book = ContactBook(storage_format="csv")
contact_book.if_header_exists()  # Calls the header function which creates a header for the csv file
