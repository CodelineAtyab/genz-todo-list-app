import csv


def save_contacts_to_file(data, filename="contacts.csv"):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Number", "Email", "Address"])
        for contact in data:
            writer.writerow([contact['name'], contact['number'], contact['email'], contact['address']])


def load_contacts_from_file(filename="contacts.csv"):
    data = []
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row:  # Check if row is not empty
                    data.append({'name': row[0], 'number': row[1], 'email': row[2], 'address': row[3]})
    except FileNotFoundError:
        print("Contacts file not found, starting with an empty list.")
    return data
