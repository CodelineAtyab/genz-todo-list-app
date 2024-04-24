import cherrypy
from app_user import AppUser
from contact import ContactRecord

class ContactBookAPI(object):
    exposed = True  # Expose the class methods as web methods

    def __init__(self):
        self.user = AppUser("default_user")

    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def POST(self):
        input_json = cherrypy.request.json
        contact = ContactRecord(input_json['name'], input_json['phone'], input_json['email'], input_json['address'])
        self.user.get_contact_book().add_contact(contact)
        return {"message": f"Contact with phone number {input_json['phone']} created."}

    def DELETE(self, name):
        self.user.get_contact_book().delete_contact(name)
        return {"message": "Contact deleted."}

    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def PUT(self, name):
        input_json = cherrypy.request.json
        self.user.get_contact_book().update_contact(name, **input_json)
        return {"message": "Contact updated."}

    @cherrypy.tools.json_out()
    def GET(self, name=None, phone=None, email=None):
        contacts = self.user.get_contact_book().search_contacts(name=name, phone=phone, email=email)
        return {"contacts": [contact.__dict__ for contact in contacts]}

if __name__ == '__main__':
    config = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.quickstart(ContactBookAPI(), '/api/contacts', config)
