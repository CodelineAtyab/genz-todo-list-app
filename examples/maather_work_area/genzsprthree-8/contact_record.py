from contact_manager import ContactManager
class ContactRecord:
    def __init__(self, name, phone_number, email, address):
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email
        self.__address = address

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, value):
        self.__phone_number = value

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if ContactManager.validate_email(value):
            self.__email = value
        else:
            raise ValueError("invalid email input")

    def get_address(self):
        return self.__address

    def set_address(self, value):
        self.__address = value