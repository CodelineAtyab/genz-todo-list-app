# class ContactRecord:
#     def __init__(self, phone_number, name, email, address):
#         self.__phone_number = phone_number
#         self.__name = name
#         self.__email = email
#         self.__address = address
#
#     def get_phone_number(self):
#         return self.__phone_number
#
#     def set_phone_number(self, inp_phone_number):
#         self.__phone_number = inp_phone_number
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, inp_name):
#         self.__name = inp_name
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, inp_email):
#         self.__email = inp_email
#
#     def get_address(self):
#         return self.__address
#
#     def set_address(self, inp_address):
#         self.__address = inp_address


import re

pattern = r"^[^\d][^@]+@[^@]+\.[^@]+"


class ContactRecord:
    def __init__(self, phone_number, name, email, address):
        self.__phone_number = phone_number
        self.__name = name
        self.__email = email
        self.__address = address

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, inp_phone_number):
        self.__phone_number = inp_phone_number

    def get_name(self):
        return self.__name

    def set_name(self, inp_name):
        self.__name = inp_name

    def set_email(self, inp_email):
        if validate_email(inp_email):
            self.__email = inp_email
        else:
            self.__email = None
            print("\nEmail not set, please update it.")

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def set_address(self, inp_address):
        self.__address = inp_address


def validate_email(inp_email):
    if re.match(pattern, inp_email):
        return True
    else:
        return False
