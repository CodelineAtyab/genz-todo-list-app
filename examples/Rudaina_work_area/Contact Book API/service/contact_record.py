

class ContactRecord:
    def __init__(self, name, phone_number, email, address=""):
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email
        self.__address = address

    def __str__(self):
        return f"Name: {self.__name}, Phone: {self.__phone_number}, Email: {self.__email}, Address: {self.__address}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address