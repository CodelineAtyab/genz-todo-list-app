from csv_contact_book import CsvContactBook
from json_contact_book import JsonContactBook
from contact_book import ContactBook
from CRUD_record import CRUDRecord
from contact_record import ContactRecord
from app_user import AppUser

APP_USERS_FILE_PATH = "./app_usernames.csv"


def main():
    requested_format = "csv"
    crud_record = None
    app_running = True
    logged_in = False
    while app_running:
        if not logged_in:
            print("1- Login with an existing username")
            print("2- Sign in as a new user")
            print("3- Exit program")
            user_login_input = int(input("Please select one of the options: "))
            while True:
                if user_login_input in [1, 2, 3]:
                    break
                else:
                    print("Invalid option")
                    user_login_input = input("Please select one of the options: ")
            if user_login_input == 1:
                user_phone = input("Please enter the phone number: ")
                user_name = input("Please enter the username: ")
                with open(APP_USERS_FILE_PATH, "a+") as app_users_file:
                    app_users_file.seek(0)
                    lines = app_users_file.readlines()
                    for index, line in enumerate(lines):
                        user_info = line.strip().split(",")
                        if user_info[0] == user_phone and user_info[1] == user_name:
                            app_user_details = AppUser(user_phone, user_name)
                            # Create JSON or CSV based on user's requirement
                            contact_book: ContactBook = None
                            if requested_format == "csv":
                                contact_book = CsvContactBook(app_user_details.get_phone_number())
                            elif requested_format == "json":
                                contact_book = JsonContactBook(app_user_details.get_phone_number())
                            contact_book.load_contacts()
                            contact_book.return_formatted_contacts()
                            crud_record = CRUDRecord(contact_book)
                            logged_in = True
                            break
                    else:
                        print("Wrong user credentials. Please try again.")

            if user_login_input == 2:
                user_phone = input("Please enter the phone number: ")
                user_name = input("Please enter the username: ")
                with open(APP_USERS_FILE_PATH, "a+") as app_users_file:
                    app_users_file.write(f"{user_phone},{user_name},\n")
                    print("\nUser created successfully.\n")

            if user_login_input == 3:
                print("\nThank you, have a good day!")
                exit()

        else:
            print("1- Add a new contact")
            print("2- Update an existing contact")
            print("3- Delete an existing contact")
            print("4- Search for a contact")
            print("5- Exit program")

            user_input = input("Please select one of the options: ")

            while True:
                if user_input and user_input.isdigit() in [1, 2, 3, 4, 5]:
                    selected_choice = int(user_input)
                    break
                else:
                    print("Invalid option")
                    user_input = input("Please select one of the options: ")

            if selected_choice == 1:
                contact_name = input("Please enter the name: ")
                contact_phone = input("Please enter the phone number: ")
                contact_email = input("Please enter the email: ")
                contact_address = input("Please enter the address: ")
                new_record = ContactRecord(contact_phone, contact_name, None, contact_address)
                new_record.set_email(contact_email)
                crud_record.create_record(new_record)

            if selected_choice == 2:
                input_value = input("Please enter contact's phone to update the values: ")
                crud_record.update_record(input_value)

            if selected_choice == 3:
                contact_phone = input("Please enter the phone number of the contact to delete: ")
                crud_record.delete_record(contact_phone)

            if selected_choice == 4:
                requested_contact = input("Please enter contact's phone number: ")
                crud_record.search_record(requested_contact)

            if selected_choice == 5:
                print("\nThank you, have a good day!")
                exit()


main()