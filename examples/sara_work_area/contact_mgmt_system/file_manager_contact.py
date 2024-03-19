CONTACTS_FILE_PATH = "./data/stored_contacts.csv"


def add_contact(contact_name, phone, email, address):
    contacts = {
        "name": contact_name,
        "phone": phone,
        "email": email,
        "address": address
    }
    try:
        phone_exists = False
        with open(CONTACTS_FILE_PATH, "r") as contact_file:
            lines = contact_file.readlines()
            for line in lines:
                existing_contact = line.split(',')
                if existing_contact[1] == phone:
                    print(f"\nContact with phone number {phone} already exists.\n")
                    phone_exists = True
                    break

        if not phone_exists:
            with open(CONTACTS_FILE_PATH, "a") as contact_file:
                contact_file.write(f"{contacts['name']},{contacts['phone']},{contacts['email']},{contacts['address']}\n")
                print("\nContact added successfully.\n")

    except FileNotFoundError:
        print("Unable to find file:", CONTACTS_FILE_PATH)
    except Exception as ex:
        print("Something went wrong.", ex)


def search_contact(search_value):
    try:
        with open(CONTACTS_FILE_PATH, "r") as contact_file:
            for line in contact_file:
                contact_info = line.strip().split(",")
                if contact_info[0].lower() == search_value.lower() or contact_info[1] == search_value or contact_info[2] == search_value:
                    return f"\nContact name: {contact_info[0]}\nContact phone number: {contact_info[1]}\nContact email: {contact_info[2]}\nContact address: {contact_info[3]}\n"
        return f"\nSorry, no contact found.\n"
    except FileNotFoundError:
        print("Unable to find file:", CONTACTS_FILE_PATH)
    except Exception as ex:
        print("Something went wrong.", ex)


def delete_contact(phone):
    try:
        contact_deleted = False
        with open(CONTACTS_FILE_PATH, "r+") as contact_file:
            lines = contact_file.readlines()
            contact_file.seek(0)
            for line in lines:
                contact_info = line.strip().split(",")
                if contact_info[1] == str(phone):
                    name, _, email, address = contact_info
                    print(f"\nContact deleted successfully\n")
                    contact_deleted = True
                else:
                    contact_file.write(line)
            contact_file.truncate()

        if not contact_deleted:
            print(f"The contact with the specified number {phone} does not exist")
    except FileNotFoundError:
        print("Unable to find file:", CONTACTS_FILE_PATH)
    except Exception as ex:
        print("Something went wrong.", ex)


def update_contact(input_value):
    try:
        contact_updated = False
        with open(CONTACTS_FILE_PATH, "r+") as contact_file:
            lines = contact_file.readlines()
            if input_value == 1:
                current_value = input("Please enter the current name: ")
            elif input_value == 2:
                current_value = input("Please enter the current phone number: ")
            elif input_value == 3:
                current_value = input("Please enter the current email address: ")
            elif input_value == 4:
                current_value = input("Please enter the current address: ")
            else:
                print("Invalid input value.")
                return

            for index, line in enumerate(lines):
                contact_info = line.strip().split(",")

                if contact_info[input_value - 1] == current_value:
                    print(f"\nContact name: {contact_info[0]}\nContact phone number: {contact_info[1]}\nContact email: {contact_info[2]}\nContact address: {contact_info[3]}\n")
                    new_value = input(f"Please enter the new {'name' if input_value == 1 else 'phone number' if input_value == 2 else 'email address' if input_value == 3 else 'address'}: ")
                    contact_info[input_value - 1] = new_value
                    lines[index] = ",".join(contact_info) + "\n"
                    contact_updated = True
                    break

            if contact_updated:
                contact_file.seek(0)
                contact_file.writelines(lines)
                contact_file.truncate()
                print("\nContact updated successfully.\n")
            else:
                print("Contact not found.")
    except FileNotFoundError:
        print("Unable to find file:", CONTACTS_FILE_PATH)
    except Exception as ex:
        print("Something went wrong.", ex)