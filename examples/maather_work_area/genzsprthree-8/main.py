from contact_manager import ContactManager
from app_user import AppUser
from contact_record import ContactRecord
from contact_book import CsvContactBook, JsonContactBook


def main():
    # testing CsvContactBook
    # create a CSV contact book
    csv_contact_book = CsvContactBook()

    # create an AppUser with the CSV contact book
    csv_user = AppUser("csv_user", "test@example.com", csv_contact_book)

    # initialize ContactManager with the user
    contact_manager = ContactManager(csv_user)

    # add a contact
    new_contact = {"phone_number": "111", "name": "name1", "email": "email1@gmail.com",
                   "address": "123 st"}
    contact_manager.add_contact(new_contact)

    # Search for a contact
    found_contact = contact_manager.search_contact("111")
    if found_contact:
        print("contact found:", found_contact.get_name())
    else:
        print("contact not found.")

    # update a contact
    contact_manager.update_contact("111", "name", "updated name1")

    # store contacts back to CSV
    contact_manager.user.contact_book.store_contacts(
        list(contact_manager.user.contact_book.contact_book_data_dict.values()))
    

    # testing JsonContactBook
    # create a JsonContactBook
    json_contact_book = JsonContactBook()

    # create an AppUser with the JSON contact book
    json_user = AppUser("json_user", "test@example.com", json_contact_book)

    # initialize ContactManager with the user
    contact_manager = ContactManager(json_user)

    # add a contact
    first_contact = {"phone_number": "111", "name": "name1", "email": "email1@gmail.com",
                   "address": "123 st"}
    contact_manager.add_contact(first_contact)

    # search for a contact
    found_contact = contact_manager.search_contact("111")
    if found_contact:
        print("contact found:", found_contact.get_name())
    else:
        print("contact not found.")

    # update a contact
    contact_manager.update_contact("111", "name", "updated name1")

    # add another contact
    scnd_contact = {"phone_number": "222", "name": "name2", "email": "email2@gmail.com",
                   "address": "124 st"}
    contact_manager.add_contact(scnd_contact)

    # delete contact
    contact_manager.delete_contact("222")


    # store contacts back to JSON
    contact_manager.user.contact_book.store_contacts(list(contact_manager.user.contact_book.contact_book_data_dict.values()))



if __name__ == "__main__":
    main()
