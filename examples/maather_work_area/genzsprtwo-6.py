import os

_STORAGE_FILE_NAME = "contact_book.csv"

_HEADER = ['name', 'phone number', 'email', 'address']

def contact_manager(csv_file = None):
    header = ['name', 'phone number', 'email', 'address']

    if not csv_file:
        csv_file = _STORAGE_FILE_NAME
        with open(csv_file, 'w', newline='') as file:
            file.write(','.join(_HEADER) + '\n')

    prompt_string = '''please input a number:
    1: add
    2: delete
    3: update 
    4: search
    5: quit
    '''

    while True:
        try:
            choice = int(input(prompt_string))
            if choice in [1, 2, 3, 4, 5]:
                break
        except ValueError:
            print("invalid input. please enter a number between 1 and 5.")

    match choice:
        case 1:
            add_contact(csv_file)
        case 2:
            delete_contact(csv_file)
        case 3:
            update_contact(csv_file)
        case 4:
            search_contact(csv_file)
        case 5:
            return


def add_contact(csv_file):
    name = input("enter name: ")
    phone_number = input("enter phone number: ")
    email = input("enter email: ")
    address = input("enter address: ")

    data = [name, phone_number, email, address]

    with open(csv_file, 'a') as file:
        file.write(','.join(data) + '\n')
    print("contact added")
    contact_manager(csv_file)

def delete_contact(csv_file):
    search_value = input("enter the data to delete using email, phone number, or name: ")
    deleted = False
    lines = []
    with open(csv_file, "r") as file:
        lines = file.readlines()
    
    with open(csv_file, "w") as file:
        for line in lines:
            values_list = [value.lower() for value in line.strip('\n').split(',')]
            print(values_list)
            if search_value.lower() not in values_list:
                file.write(line)
            else: 
                deleted = True
    if deleted:
        print("contact deleted.")
    else:
        print("unable to find a match")
    # go back to the main function
    contact_manager(csv_file)

def update_contact(csv_file):
    search_value = input("enter the data to update using email, phone number, or name: ")
    field_to_update = input("which field do you want to update (ie: email): ")
    new_value = input(f"enter the new {field_to_update} value: ").lower()
    updated = True

    with open(csv_file, "r") as file:
        lines = file.readlines()

    with open(csv_file, "w") as file:
        for line in lines:
            values_list = [value.lower() for value in line.strip('\n').split(',')]
            if search_value.lower() not in values_list:
                file.write(line)
            else: 
                # update the row and write new value
                match field_to_update:
                    case "name":
                        values_list[0] = new_value
                    case "phone number":
                        values_list[1] = new_value
                    case "email":
                        values_list[2] = new_value
                    case "address":
                        values_list[3] = new_value
                    case _:
                        updated = False
                file.write(",".join(values_list) + "\n")
    if not updated:
        print("unable to update due to wrong field value")
    else:
        print("updated")
        contact_manager(csv_file)
    
def search_contact(csv_file, data_type = None):
    if not data_type:
        data_type = input("would you like to search using email, phone number, name, or address? ")
    if data_type.lower() in ["email", "phone number", "name", "address"]:
        search_value = input("enter search value: ")
        found = False
        with open(csv_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                values_list = line.strip('\n').split(',')
                if values_list[["name", "phone number", "email", "address"].index(data_type.lower())] == search_value:
                    found = True 
                    print(values_list)
            if not found:       
                print("unable to find a match.")
    else:
        print("Invalid input.")
    contact_manager(csv_file)

contact_manager()