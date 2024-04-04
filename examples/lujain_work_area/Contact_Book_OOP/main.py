# main.py

from contact_record import ContactRecord
from contact_book import JSONContactBook, CSVContactBook

if __name__ == "__main__":
    # Create JSON contact book
    json_contact_book = JSONContactBook()

    # Adding contacts to JSON contact book
    contact1 = ContactRecord("Tom", "1234567890", "tom@example.com", "123 St")
    contact2 = ContactRecord("Kate", "9876543210", "kate@example.com", "456 St")
    json_contact_book.add_contact(contact1)
    json_contact_book.add_contact(contact2)

    # Save JSON contact book to file
    json_contact_book.save("contacts.json")  # Sample JSON data will be saved here

    # Load JSON contact book from file
    loaded_json_contact_book = JSONContactBook()
    loaded_json_contact_book.load("contacts.json")  # Sample JSON data will be loaded from here

    # Searching for a contact in JSON contact book
    results_json = loaded_json_contact_book.search_contact("Tom")
    print("Contacts from JSON:")
    for contact in results_json:
        print(contact.to_dict())

    # Create CSV contact book
    csv_contact_book = CSVContactBook()

    # Adding contacts to CSV contact book
    contact3 = ContactRecord("Sally", "3333333333", "sally@example.com", "863 St")
    contact4 = ContactRecord("Jessie", "2323232332", "jessie@example.com", "101 St")
    csv_contact_book.add_contact(contact3)
    csv_contact_book.add_contact(contact4)

    # Save CSV contact book to file
    csv_contact_book.save("contacts.csv")  # Sample CSV data will be saved here

    # Load CSV contact book from file
    loaded_csv_contact_book = CSVContactBook()
    loaded_csv_contact_book.load("contacts.csv")  # Sample CSV data will be loaded from here

    # Searching for a contact in CSV contact book
    results_csv = loaded_csv_contact_book.search_contact("Sally")
    print("\nContacts from CSV:")
    for contact in results_csv:
        print(contact.to_dict())

