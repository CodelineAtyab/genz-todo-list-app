from contact_record import ContactRecord


class CRUDRecord:
    def __init__(self, input_file):
        self.__input_file = input_file

    def create_record(self, contact: ContactRecord):
        self.__input_file.store_contact(contact)

    def update_record(self, phone_number: str):
        if phone_number in self.__input_file.contact_book_data_dict:
            contact_info = self.__input_file.contact_book_data_dict[phone_number]
            print(f"\nContact name: {contact_info["name"]}\nContact phone number: {phone_number}\n"
                  f"Contact email: {contact_info["email"]}\nContact address: {contact_info["address"]}\n")
            contact_name = input("Please enter the updated name: ")
            contact_phone = input("Please enter the updated phone number: ")
            contact_email = input("Please enter the updated email: ")
            contact_address = input("Please enter the updated address: ")
            new_record = ContactRecord(contact_phone, contact_name, contact_email, contact_address)
            self.__input_file.update_contact(phone_number, new_record)
        else:
            print("Contact not found.")

    def search_record(self, phone_number: str):
        if phone_number in self.__input_file.contact_book_data_dict:
            contact_info = self.__input_file.contact_book_data_dict[phone_number]
            print(f"\nContact name: {contact_info["name"]}\nContact phone number: {phone_number}\n"
                  f"Contact email: {contact_info["email"]}\nContact address: {contact_info["address"]}\n")
        else:
            print("Contact not found.")

    def delete_record(self, phone_number: str):
        self.__input_file.delete_contact(phone_number)
