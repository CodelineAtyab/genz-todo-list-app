import os
import csv

info_line = ['Name', 'Phone', 'Email', 'Address']
file_path = "./contact_data.csv"


def append_contact(data, is_row):
    """
    append one row of contact information to the csv file if
    it exists and if not create it and append the header
    :param data: a list of contact info [ name, phone, email, address]
    :param is_row: if the entered data is just a row(True) or a list (False)
    :return: message for any exceptions error
    """
    try:
        if os.path.exists(file_path):
            if is_row:
                with open(file_path, 'a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(data)
            else:
                with open(file_path, 'w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    for row in data:
                        writer.writerow(row)
        else:
            with open(file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(info_line)
                writer.writerow(data)

            print(f'{file_path} has been created')

    except FileNotFoundError:
        print("Unable to locate file:", file_path)
    except Exception as ex:
        print("Something went wrong.", ex)


def delete_contact_data(key, value):
    """

    :param key: column index (Name=0, Phone=1, Email=2)
    :param value: a unique identifier (e.g., name or email) for existing contact info
    :return: delete message of its deleted successfully
                or if the contact of the value couldn't be found
    """
    deleted = False
    data = read_csv()
    for row in data:
        if row[key] == value:
            data.remove(row)
            deleted = True
    append_contact(data, False)
    if deleted:
        print("Contact deleted successfully\n")
    else:
        print("Contact not found\n")


def read_csv():
    try:
        with open(file_path, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            data = list(reader)
        return data

    except FileNotFoundError:
        print("Unable to locate file:", file_path)
    except Exception as ex:
        print("Something went wrong.", ex)


def search(key, value):
    """

    :param key: column index (Name=0, Phone=1, Email=2)
    :param value: a unique identifier (e.g., name or email) for existing contact info
    :return: the full contact information of the identifier
            or a message if the contact info doesn't exist
    """
    data = read_csv()
    found = False
    for row in data:
        if row[key] == value:
            print(f'Contact data for {value} is : {row}')
            found = True
    if not found:
        print("This Contact Doesn't Exist \n")


def update(identifier, original, updated):
    is_updated = False
    data = read_csv()
    i = 0
    for row in data:
        i += 1
        if row[0] == original:
            data[i-1][identifier] = updated
            is_updated = True
    append_contact(data, False)
    if is_updated:
        print("Contact Updated successfully\n")
    else:
        print("Contact not found\n")
