from models.contact_record import ContactRecord
from models.app_user import AppUser


def main():

    username = "John Doe"
    user_email = "john@example.com"
    user_phone = "1234567890"
    # Create an instance of AppUser
    user1 = AppUser(username,user_email, user_phone)
    contact1 = ContactRecord("Bob", "4567890123", "bob@example.com", "456 Elm St")
    user1.contact_book.add(contact1)

    # Add contacts to the ContactBook of user1
    contact2 = ContactRecord("Alice", "9876543210", "alice@example.com", "123 Main St")
    contact3 = ContactRecord("Bob", "4567890123", "bob@example.com", "456 Elm St")
    user1.contact_book.add(contact2)
    user1.contact_book.add(contact3)

    print("-------------------------------")
    print("User Information:")
    print("Name:", user1.get_name())
    print("Email:", user1.get_email())
    print("Phone:", user1.get_phone())

    # Test operations
    print("Contacts for", user1.get_name())
    for contact in user1.contact_book.contacts:
        print(contact)

    # Search for a contact
    search_email = "alice@example.com"
    found_contact = user1.contact_book.search(search_email)
    if found_contact:
        print("Found contact for", search_email, ":", found_contact)
    else:
        print("Contact for", search_email, "not found")

    # Update a contact
    updated_contact = ContactRecord("Alice", "9876543210", "alice@example.com", "456 New St")
    user1.contact_book.update("alice@example.com", updated_contact)
    print("Updated contact:", user1.contact_book.search("alice@example.com"))

    # Delete a contact
    user1.contact_book.delete("bob@example.com")
    print("Contact for bob@example.com deleted")

    # Save contacts to a file
    user1.contact_book.save_contact()

    # Create a second instance of AppUser
    user2 = AppUser("Jane Smith", "jane@example.com", "9876543210")

    print("-------------------------------")
    print("User Information:")
    print("User2 Name:", user2.get_name())
    print("User2 Email:", user2.get_email())
    print("User2 Phone:", user2.get_phone())

    # Create more contacts for user2
    new_contact2 = ContactRecord("Bob", "4567890123", "bob@example.com", "456 Elm St")
    user2.contact_book.add(new_contact2)

    new_contact3 = ContactRecord("Eve", "7890123456", "eve@example.com", "789 Oak St")
    user2.contact_book.add(new_contact3)

    # Print the contacts for user2
    print("Contacts for", user2.get_name())
    for contact in user2.contact_book.contacts:
        print(contact)

    user2.contact_book.save_contact()


if __name__ == "__main__":
    main()