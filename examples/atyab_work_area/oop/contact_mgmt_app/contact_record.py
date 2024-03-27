class ContactRecord:
    # TODO: Define getters and setters for the following fields
    # TODO: Change the related code accordingly
    def __init__(self, phone_number, name, email):
        self.__phone_number = phone_number
        self.__name = name
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, inp_phone_number):
        self.__phone_number = inp_phone_number
