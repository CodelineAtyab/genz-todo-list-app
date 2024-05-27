class ContactRecord:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address
        }

    def __repr__(self):
        return f"ContactRecord(name={self.name}, phone_number={self.phone_number}, email={self.email}, address={self.address})"
