import os

CONTACT_FILE_PATH = "C:/Users/71519/Documents/genz-todo-list-app/examples/abbas_work_area/data/store_contacts.csv"


def write_heading():
    open_write_file("Name,Contact,Email,Address\n", 'w')  # writes heading of csv


def if_header_exists():
    if not os.path.exists(CONTACT_FILE_PATH):  # checks if file exists
        write_heading()


def open_write_file(data="", state="r"):  # Handles file operations "w, a, and r"
    with open(CONTACT_FILE_PATH, state) as contact_file:
        if state == "a" or state == "w":
            contact_file.write(data)
        elif state == "r":
            return [x.strip() for x in contact_file.readlines()]


try:
    def store_contact(name, contact, email, address):  # Stores new contacts
        """
        Creates and stores records in csv file.
        Name, Contact, Email, Address.
        """
        open_write_file(f"{name}, {contact}, {email}, {address}" + '\n', 'a')
        print("Contact added successfully!")
except FileNotFoundError as ff:
    print("File not found", ff)
except Exception as ex:
    print("Error with writing file_manager", ex)


def delete_contact(incoming):
    """
        Deletes existing results based on name
        input: Abbas
        output: Deleted Successfully!
    """
    result_to_del = read_contact(incoming)
    result_split = result_to_del.split(",")
    all_lines = open_write_file("", 'r')
    result = []

    try:
        for contact in all_lines[1:]:
            contact_details = contact.split(",")
            if contact_details[1] not in result_split[1]:
                result.append(contact + '\n')
        write_heading()
        for contact in result:
            open_write_file(contact, 'a')

        print("Record Deleted Successfully!")

    except Exception as ex:
        print("Error", ex)


def update_contact(old_info, name, contact, email, address):
    """
        Updates existing results based on name
        input: Abbas
        output: Updated Successfully!
    """
    updated_line = read_contact(old_info)
    updated = updated_line.split(',')
    all_lines = open_write_file("", 'r')
    result = []

    try:
        for contacts in all_lines[1:]:
            contact_details = contacts.split(",")
            if contact_details[1] not in updated[1]:
                result.append(contacts)
            elif contact_details[1] in updated[1]:
                result.append(f"{name}, {contact}, {email}, {address}")

        write_heading()

        for contacts in result:
            open_write_file(contacts + '\n', 'a')
        print("Updated Successfully!")
    except Exception as ex:
        print("Error", ex)


def read_contact(search):
    """
    Search for a specific record based on unique key, in this case the name.
    e.g: input: John Doe
         output: Name: John Doe, Phone Number: 1234, Email: John@gmail.com, Address: Oman
    """
    try:
        contacts = open_write_file()
        for contact in contacts[1:]:
            contact_details = contact.split(",")

            if contact_details[1].strip().lower() == search.strip().lower():
                return f"[Name: {contact_details[0]}, Phone Number: {contact_details[1]}, Email: {contact_details[2]}, Address: {contact_details[3]}]"
        return "Not found"
    except Exception as ex:
        print("Error", ex)
