class ContactRecord:
    # TODO: Define getters and setters for the following fields
    # TODO: Change the related code accordingly

        def __init__(self, name, phone_number, email, address):
            self.name = name
            self.phone_number = phone_number
            self.email = email
            self.address = address

        def __repr__(self):
            return f"ContactRecord(name={self.name}, phone_number={self.phone_number}, email={self.email}, address={self.address})"

"""         def get_phone_number(self):
            return self.__phone_number

         def set_phone_number(self, inp_phone_number):
             self.__phone_number = inp_phone_number
"""