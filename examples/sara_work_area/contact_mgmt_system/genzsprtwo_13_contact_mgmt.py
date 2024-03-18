import file_manager_contact


def main():
    app_running = True
    while app_running:
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
            # contact_name, contact_phone, contact_email, contact_address = input(
            #     "Please enter the contact name, phone, email, and address in order: ").split()
            file_manager_contact.add_contact(contact_name, contact_phone, contact_email, contact_address)

        if selected_choice == 2:
            print(" 1- Name\n 2- Phone\n 3- Email\n 4- Address")
            input_value = int(input("Select the value to update: "))
            file_manager_contact.update_contact(input_value)

        if selected_choice == 3:
            contact_phone = int(input("Please enter the phone number of the contact to delete: "))
            file_manager_contact.delete_contact(contact_phone)

        if selected_choice == 4:
            requested_contact = input("Please enter the contact name, phone, or email: ")
            print(file_manager_contact.search_contact(requested_contact))

        if selected_choice == 5:
            print("\nThank you, have a good day!")
            exit()


main()
