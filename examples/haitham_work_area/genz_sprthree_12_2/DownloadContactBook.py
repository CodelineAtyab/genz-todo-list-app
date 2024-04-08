
def export_as_txt(contacts, filename="contacts_export.txt"):
    with open(filename, 'w') as file:
        for contact in contacts:
            contact_details = f"{contact.name}, {contact.phone}, {contact.email}, {contact.address}\n"
            file.write(contact_details)
    print(f"Contacts successfully downloaded as TXT to {filename}.")


def export_as_json(contacts, filename="contacts_export.json"):
    import json
    contacts_data = [
        {"name": contact.name, "phone": contact.phone, "email": contact.email, "address": contact.address} for
        contact in contacts]
    with open(filename, 'w') as file:
        json.dump(contacts_data, file, indent=4)
    print(f"Contacts successfully downloaded as JSON to {filename}.")


