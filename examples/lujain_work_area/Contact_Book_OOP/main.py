# main.py

from contact_record import ContactRecord
from app_user import AppUser

if __name__ == "__main__":
    # Create an AppUser
    user = AppUser("JohnDoe", "john@example.com")

    # Adding contacts to the user's ContactBook
    contact1 = ContactRecord("Tom", "1234567890", "tom@example.com", "123 St")
    contact2 = ContactRecord("Kate", "9876543210", "kate@example.com", "456 St")
    user.add_contact(contact1)
    user.add_contact(contact2)

    # Save the ContactBook to a JSON file
    user.save_contact_book("contacts", format='json')

    # Load the ContactBook from the JSON file
    user.load_contact_book("contacts", format='json')

    # Searching for a contact in the ContactBook
    results = user.search_contact("Kate")
    print("Contacts found:")
    for contact in results:
        print(contact.to_dict())
