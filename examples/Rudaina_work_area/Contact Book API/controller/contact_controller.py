import cherrypy
import json
from models.contact_record import ContactRecord
from models.contatc_book import ContactBook
json_file = 'models/data/contacts.json'


class ContactAPI:
    exposed = True

    def __init__(self):
        self.contact_book = ContactBook(json_file)

    def _create_response(self, status, data):
        return {"status": status, "data": data}

    @cherrypy.tools.json_out()
    def GET(self, email=None):
        if email:
            contact = self.contact_book.search(email)
            if contact:
                return self._create_response("SUCCESS", contact.to_dict())
            else:
                return self._create_response("FAIL", "Contact not found")
        else:
            contacts = [contact.to_dict() for contact in self.contact_book.contacts]
            return self._create_response("SUCCESS", contacts)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        data = cherrypy.request.json
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')
        address = data.get('address')
        if not (name and phone and email and address):
            return self._create_response("FAIL", "Invalid request parameters")
        contact = ContactRecord(name, phone, email, address)
        self.contact_book.add(contact)
        return self._create_response("SUCCESS", {"message": "Contact added successfully"})

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, email):
        data = cherrypy.request.json
        updated_contact = ContactRecord(**data)
        if not self.contact_book.update(email, updated_contact):
            return self._create_response("FAIL", "Contact not found")
        return self._create_response("SUCCESS", {"message": "Contact updated successfully"})

    def DELETE(self, email):
        if not self.contact_book.delete(email):
            return self._create_response("FAIL", "Contact not found")
        return self._create_response("SUCCESS", {"message": "Contact deleted successfully"})
