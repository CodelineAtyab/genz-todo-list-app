import os

CONTACTS_FILE = "./contacts.csv"

def rewrite_file_with_list(list_of_lines):
    del list_of_lines[0]
    os.remove(CONTACTS_FILE)
    create_file_if_not_exist()
    for item in list_of_lines:
        add_contact(item.strip())


def create_file_if_not_exist():
    header = ",".join(["Name", "Phone", "Email", "Address"])
    if not os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "w") as data_store:
            data_store.write(header + "\n")


def add_contact(contact):
    with open(CONTACTS_FILE, "a") as file_writer:
        file_writer.write(contact + "\n")    


def delete_contact(contact):
    is_found = False
    with open(CONTACTS_FILE, "r") as file_reader:

        lines_in_file = file_reader.readlines()
        for index, item in enumerate(lines_in_file):
            if contact in item:
                is_found = True
                del lines_in_file[index]
    
    if is_found:
        rewrite_file_with_list(lines_in_file)
    else:
        print("Not Found. Try again.")

                
def update_contact(contact, updated_contact):
    is_found = False
    with open(CONTACTS_FILE, "r") as file_reader:

        lines_in_file = file_reader.readlines()
        for index, item in enumerate(lines_in_file):
            if contact in item:
                is_found = True
                lines_in_file[index] = updated_contact
    
    if is_found:
        rewrite_file_with_list(lines_in_file)
    else:
        print("Not Found. Try again.")
                

def search_contact(contact):
    is_found = False
    index_of_found = 0
    with open(CONTACTS_FILE, "r") as file_reader:

        lines_in_file = file_reader.readlines()
        for index, item in enumerate(lines_in_file):
            if contact in item:
                is_found = True
                index_of_found = index
    
    if is_found:
        return lines_in_file[index_of_found].strip()
    else:
        return "Not Found. Try again."


## Test Cases
# print(search_contact("Name: Ziyad"[6:]))
# print("Name: Ziyad"[6:])
# update_contact("John Doe", "John Doe does not like fish")
# delete_contact("John Doe")
# create_file_if_not_exist()
# add_contact("Oya,Zigi,Bro")
    