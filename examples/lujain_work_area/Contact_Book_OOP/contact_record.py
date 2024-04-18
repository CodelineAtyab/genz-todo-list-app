# contact_record.py

class ContactRecord:
    def __init__(self, name, phone, email, address):
        """
        Initialize a ContactRecord object with name, phone, email, and address.
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        """
        Convert the ContactRecord object to a dictionary.
        """
        return {'Name': self.name, 'Phone': self.phone, 'Email': self.email, 'Address': self.address}

    @classmethod
    def from_dict(cls, data):
        """
        Create a ContactRecord object from a dictionary.
        """
        return cls(data['Name'], data['Phone'], data['Email'], data['Address'])
