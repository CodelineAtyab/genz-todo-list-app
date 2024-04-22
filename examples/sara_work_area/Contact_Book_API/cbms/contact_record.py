class ContactRecord:
    def __init__(self, phone_number, name, email):
        self.phone_number = phone_number
        self.name = name
        self.email = email

        if not self.__is_data_valid():
            raise Exception("Invalid data in the record")

    def __is_data_valid(self):
        if not self.phone_number.isdigit() or not self.name or not self.email or '@' not in self.email or '.' not in self.email:
            return False
        return True
