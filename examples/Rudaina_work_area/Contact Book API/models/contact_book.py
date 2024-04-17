

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)

    def search(self, email):
        for contact in self.contacts:
            if contact.email == email:
                return contact
        return None

    def update(self, email, updated_contact):
        for i, contact in enumerate(self.contacts):
            if contact.email == email:
                self.contacts[i] = updated_contact
                return True
        return False

    def delete(self, email):
        for i, contact in enumerate(self.contacts):
            if contact.email == email:
                del self.contacts[i]
                return True
        return False
