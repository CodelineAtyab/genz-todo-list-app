# this application will provide a contact list
from contact_functions import add_contact, edit_contact, search_contacts, delete_contact
from file_operation import load_contacts_from_file, save_contacts_to_file
data = []


def main():
    global data
    data = load_contacts_from_file()  # Load contacts at the start
    app_status = True
    while app_status:
        print('(1) Add Contact')
        print('(2) Edit Contact')
        print('(3) Delete Contact')
        print('(4) Search the Contact List')
        print('(5) Exit')

        user_input = input('Please select an option: ')
        if user_input and user_input.isdigit():
            user_option = int(user_input)
            if user_option == 1:
                add_contact(data)
                save_contacts_to_file(data)
            elif user_option == 2:
                edit_contact(data)
                save_contacts_to_file(data)
            elif user_option == 3:
                delete_contact(data)
                save_contacts_to_file(data)
            elif user_option == 4:
                search_contacts(data)
                save_contacts_to_file(data)
            elif user_option == 5:
                print('Exiting the application.')
                app_status = False
            else:
                print('Oops! Wrong number perhaps? Try again.')


if __name__ == '__main__':
    main()
