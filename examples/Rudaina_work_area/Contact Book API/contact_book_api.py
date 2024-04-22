import cherrypy
from models.contact_record import ContactRecord
from models.app_user import AppUser
from models.contatc_book import ContactBook


class ContactBookAPI:
    exposed = True

    def __init__(self, username, email, phone):
        self.user = AppUser(username, email, phone)
        self.contact_book = self.user.contact_book

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def GET(self, email):
        if email:
            contact = self.contact_book.search(email)
            if contact:
                return contact.to_dict()
            else:
                raise cherrypy.HTTPError(404, "Contact not found")
        else:
            return [contact.to_dict() for contact in self.contact_book.contacts]

    @cherrypy.tools.json_in()
    def POST(self):
        data = cherrypy.request.json
        contact = ContactRecord(**data)
        self.contact_book.add(contact)
        return {"message": "Contact added successfully"}

    @cherrypy.tools.json_in()
    def PUT(self, email):
        data = cherrypy.request.json
        updated_contact = ContactRecord(**data)
        if self.contact_book.update(email, updated_contact):
            return {"message": "Contact updated successfully"}
        else:
            raise cherrypy.HTTPError(404, "Contact not found")

    def DELETE(self, email):
        if self.contact_book.delete(email):
            return {"message": "Contact deleted successfully"}
        else:
            raise cherrypy.HTTPError(404, "Contact not found")

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
    username = "John Doe"
    user_email = "john@example.com"
    user_phone = "1234567890"
    cherrypy.tree.mount(ContactBookAPI(username, user_email, user_phone), '/contacts')
    cherrypy.engine.start()
    cherrypy.engine.block()
