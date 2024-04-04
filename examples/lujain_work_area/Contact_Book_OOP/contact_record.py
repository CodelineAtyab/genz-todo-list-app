# contact_record.py

class ContactRecord:
    def __init__(self, name, phone, email, address):
        """
        Initialize a ContactRecord object with name, phone, email, and address.

        Args:
            name (str): The name of the contact.
            phone (str): The phone number of the contact.
            email (str): The email address of the contact.
            address (str): The address of the contact.
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        """
        Convert the ContactRecord object to a dictionary.

        Returns:
            dict: A dictionary representation of the ContactRecord.
        """
        return {'Name': self.name, 'Phone': self.phone, 'Email': self.email, 'Address': self.address}

    @classmethod
    def from_dict(cls, data):
        """
        Create a ContactRecord object from a dictionary.

        Args:
            data (dict): The dictionary containing contact information.

        Returns:
            ContactRecord: A ContactRecord object created from the dictionary.
        """
        return cls(data['Name'], data['Phone'], data['Email'], data['Address'])
