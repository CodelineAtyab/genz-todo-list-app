from app_user import AppUser
from contact import ContactRecord

def main_menu():
    username = input("Enter your username: ")
    user = AppUser(username)

    choices = {
        '1': "Add",
        '2': "Delete",
        '3': "Update",
        '4': "List All",
        '5': "Download",
        '6': "Exit"
    }

    while True:
        print("\nContact Book Menu:")
        for key, value in choices.items():
            print(f"{key}. {value}")
        selection = input("Choose an option: ")

        if selection == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            user.get_contact_book().add_contact(ContactRecord(name, phone, email, address))
        elif selection == '2':
            name = input("Enter the name of the contact to delete: ")
            user.get_contact_book().delete_contact(name)
        elif selection == '3':
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name or press enter to skip: ")
            new_phone = input("Enter new phone number or press enter to skip: ")
            new_email = input("Enter new email or press enter to skip: ")
            new_address = input("Enter new address or press enter to skip: ")
            user.get_contact_book().update_contact(old_name, new_name=new_name, new_phone=new_phone, new_email=new_email, new_address=new_address)
        elif selection == '4':
            user.get_contact_book().list_contacts()
        elif selection == '5':
            format_type = input("Download as (CSV, JSON, TXT): ").upper()
            user.get_contact_book().download_contacts(format_type)
        elif selection == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main_menu()