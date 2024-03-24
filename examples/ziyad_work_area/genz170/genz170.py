import file_manager

choice = 0
while choice != 5:
    
    print("-----Contact Book Application----- ")
    print("(1) Add Contact ")
    print("(2) Delete Contact ")
    print("(3) Update Contact ")
    print("(4) Search Contact ")
    print("(5) Exit ")
    choice = int(input("Enter the option number: "))

    # Add Contact
    if choice == 1:
        add_input = input("Enter Contact to Add: ")
        file_manager.add_contact(add_input)
        print("Added Successfully!")

    # Delete Contact
    elif choice == 2:
        delete_input = input("Enter Contact to Delete: ")
        file_manager.delete_contact(delete_input)

    # Update Contact
    elif choice == 3:
        update_input = input("Enter Contact to Update: ")
        update_new_input = input("Enter The Updated Contact: ")
        file_manager.update_contact(update_input, update_new_input)

    # Search Contact
    elif choice == 4:
        search_input = input("Enter Contact Name to Search: ")
        print(file_manager.search_contact(search_input))
