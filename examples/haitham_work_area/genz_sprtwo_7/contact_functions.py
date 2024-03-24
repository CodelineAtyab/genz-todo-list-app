def add_contact(data):
    name = input('Name: ')
    number = input('Number: ')
    email = input('E-mail: ')
    address = input('Address: ')
    data.append({'name': name, 'number': number, 'email': email, 'address': address})
    print("Contact added successfully.")


def edit_contact(data):
    name_to_edit = input('Enter the name of the contact you would like to edit: ')
    for contact in data:
        if contact['name'].lower() == name_to_edit.lower():
            print(f"Editing contact: {contact['name']}")
            contact['name'] = input("Enter new name (or leave blank to keep current): ") or contact['name']
            contact['number'] = input("Enter new number (or leave blank to keep current): ") or contact['number']
            contact['email'] = input("Enter new email (or leave blank to keep current): ") or contact['email']
            contact['address'] = input("Enter new address (or leave blank to keep current): ") or contact['address']
            print("Contact updated successfully.")
            return
    print("Contact not found.")


def delete_contact(data):
    name_to_delete = input("Enter the name of the contact to delete: ")
    initial_length = len(data)
    data[:] = [contact for contact in data if contact['name'].lower() != name_to_delete.lower()]
    if len(data) < initial_length:
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def search_contacts(data):
    search_query = input("Enter contact name: ").lower()
    found_contacts = [contact for contact in data if search_query in contact['name'].lower() or
                      search_query in contact['number'].lower() or
                      search_query in contact['email'].lower() or
                      search_query in contact['address'].lower()]
    if found_contacts:
        print("Found contacts:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Number: {contact['number']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found.")
