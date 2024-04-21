class ContactRecord:
    def __init__(self, phone_number, name, email):
        self.phone_num = phone_number
        self.name = name
        self.email = email

        if not self.__is_data_valid():
            raise Exception("Invalid data in the record")

    def __is_data_valid(self):
        return True
