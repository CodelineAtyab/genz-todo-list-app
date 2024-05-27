class AppUser:
    def __init__(self, phone_number, name):
        self.__phone_number = phone_number
        self.__name = name

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, inp_phone_number):
        self.__phone_number = inp_phone_number

    def get_name(self):
        return self.__name

    def set_name(self, inp_name):
        self.__name = inp_name

