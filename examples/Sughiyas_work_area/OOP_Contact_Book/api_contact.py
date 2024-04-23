import cherrypy
import json
from ContactBook import ContactBook
# Assuming you have an existing ContactBook class defined elsewhere


class ContactBookAPI:
    def __init__(self):
        self.contact_book = ContactBook()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def add_contact(self, name, phone, email, address):
        # Assuming ContactBook.add_contact returns True on success
        success = self.contact_book.add_contact(name, phone, email, address)
        if success:
            return {'message': 'Contact added successfully'}
        else:
            cherrypy.response.status = 400  # Bad request
            return {'error': 'Failed to add contact'}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def delete_contact(self, contact_id):
        # Assuming ContactBook.delete_contact returns True on success
        success = self.contact_book.delete_contact(contact_id)
        if success:
            return {'message': 'Contact deleted successfully'}
        else:
            cherrypy.response.status = 404  # Not found
            return {'error': 'Contact not found'}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def update_contact(self, contact_id, phone):
        # Assuming ContactBook.update_contact returns True on success
        success = self.contact_book.update_contact(contact_id, phone)
        if success:
            return {'message': 'Contact updated successfully'}
        else:
            cherrypy.response.status = 404  # Not found
            return {'error': 'Contact not found'}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def search_contacts(self, name=None, email=None, phone=None):
        # Assuming ContactBook.search_contacts returns a list of contacts
        contacts = self.contact_book.search_contacts(name=name, email=email, phone=phone)
        return contacts


if __name__ == '__main__':
    # Configure CherryPy to serve the API
    config = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    cherrypy.quickstart(ContactBookAPI(), '/api', config=config)
