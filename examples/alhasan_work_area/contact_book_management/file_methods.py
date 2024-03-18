import os

FILE_STORAGE_PATH = "./contact.store.csv"


def get_individual_fields():
    with open(FILE_STORAGE_PATH, "r") as data_store_file:
        reader = [line.strip().split(",") for line in data_store_file.readlines()]
        return reader


def create_file_if_not_exist():
    headers = ",".join(["name", "phone", "email", "address"])
    if not os.path.exists(FILE_STORAGE_PATH):
        with open(FILE_STORAGE_PATH, "w") as data_store_file:
            data_store_file.write(headers + '\n')


def add_contact(name, phone, email, address):
    contact_details = [name, phone, email, address]
    with open(FILE_STORAGE_PATH, "a") as data_store_file:
        data_store_file.write(",".join(contact_details) + '\n')
    print("The following contact details,", contact_details, " have been added")


def delete_contact(name):
    contacts = []
    fields = get_individual_fields()
    for row in fields:
        if row[0] != name:
            contacts.append(row)

    with open(FILE_STORAGE_PATH, "w") as data_store_file:
        for contact in contacts:
            data_store_file.write(",".join(contact) + "\n")

    print("The contact with the specified name", name, "was deleted")


def update_contact(name, phone, email, address):
    contact_details = [name, phone, email, address]
    fields = get_individual_fields()
    with open(FILE_STORAGE_PATH, "w") as data_store_file:
        for row in fields:
            if row[0] == contact_details[0]:
                row[1:] = contact_details[1:]
            data_store_file.write(",".join(row) + "\n")

    print("The contact with the details:", contact_details, "was successfully updated")


def search_contact(name):
    fields = get_individual_fields()
    contacts_found = False
    for row in fields:
        if row[0] == name:
            print("Contact Details:")
            print("Name: ", row[0])
            print("Phone: ", row[1])
            print("Email: ", row[2])
            print("Address: ", row[3])
            return
    if not contacts_found:
        print("Contacts not found!")
