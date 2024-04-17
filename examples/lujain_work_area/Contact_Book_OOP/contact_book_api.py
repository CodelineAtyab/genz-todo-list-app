import cherrypy
import json
from contact_record import ContactRecord
from app_user import AppUser

class ContactBookAPI(object):
    def __init__(self):
        self.user = AppUser("JohnDoe", "john@example.com")

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def add_contact(self):
        data = cherrypy.request.json

        #  generates an instance of cherrypy.HTTPError indicating an invalid request
        if not all(key in data for key in ['name', 'phone', 'email', 'address']):
            raise cherrypy.HTTPError(400, 'Invalid Request')

        contact = ContactRecord(data['name'], data['phone'], data['email'], data['address'])
        self.user.add_contact(contact)
        return {'message': f"A new contact with the phone number: {data['phone']} has been created successfully."}

    @cherrypy.expose
    def delete_contact(self, contact_id):
        try:
            self.user.delete_contact(contact_id)
            return 'Deleted successfully.'
        except:
            # generates an instance of cherrypy.HTTPError indicating contact not found
            raise cherrypy.HTTPError(404, 'Error: Contact not found')

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update_contact(self, contact_id):
        data = cherrypy.request.json
        try:
            self.user.update_contact(contact_id, data)
            return {'message': 'Updated successfully.'}
        except:
            raise cherrypy.HTTPError(404, 'Error: Contact not found')

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def search_contact(self, name=None, email=None, phone=None):
        if name:
            results = self.user.search_contact(name)
        elif email:
            results = self.user.search_contact(email)
        elif phone:
            results = self.user.search_contact(phone)
        else:
            raise cherrypy.HTTPError(400, 'Invalid Request')

        return [contact.to_dict() for contact in results]

if __name__ == '__main__':
    cherrypy.quickstart(ContactBookAPI())
