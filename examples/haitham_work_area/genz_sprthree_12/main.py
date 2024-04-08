from AppUser import (AppUser)


def print_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. List All Contacts")
    print("5. Download All Contacts")
    print("6. Exit")


def get_contact_details():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    return name, phone, email, address


def main():
    print("Welcome to the Contact Book Application!")
    username = input("Please enter your username: ")
    email = input("Please enter your email: ")
    storage_format = input("Please choose a storage format (csv, json, txt): ").lower()

    user = AppUser(username, email, storage_format)

    while True:
        print_menu()
        choice = input("Select an option: ")

        if choice == '1':
            name, phone, email, address = get_contact_details()
            user.contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            email = input("Enter the email of the contact to delete: ")
            user.contact_book.delete_contact(email)

        elif choice == '3':
            email = input("Enter the email of the contact to update: ")
            print("Enter new details (press enter to skip):")
            name, phone, new_email, address = get_contact_details()
            user.contact_book.update_contact(email, name=name, phone=phone, new_email=new_email if new_email else None,
                                             address=address)

        elif choice == '4':
            user.contact_book.list_contacts()

        elif choice == '5':
            filename = input("Enter filename to save contacts (including file extension, e.g., 'contacts.csv'): ")
            user.contact_book.save_contacts(filename)
            print(f"All contacts have been saved to {filename}.")

        elif choice == '6':
            print("Thank you for using the Contact Book. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
