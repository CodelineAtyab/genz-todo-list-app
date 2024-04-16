import cherrypy
from ..models.contact_record import ContactRecord
from ..models.app_user import AppUser


class ContactBookAPI:
    exposed = True

    def __init__(self):
        self.user1 = AppUser("user1", "user1@example.com", "1234567890")

    @cherrypy.tools.json_out()
    def GET(self, email=None):
        if email:
            contact = self.user1.contact_book.search(email)
            if contact:
                return contact.__dict__
            else:
                raise cherrypy.HTTPError(404, "Contact not found")
        else:
            return [contact.__dict__ for contact in self.user1.contact_book.contacts]

    @cherrypy.tools.json_in()
    def POST(self):
        data = cherrypy.request.json
        contact = ContactRecord(**data)
        self.user1.contact_book.add(contact)
        return {"message": "Contact added successfully"}

    @cherrypy.tools.json_in()
    def PUT(self, email):
        data = cherrypy.request.json
        updated_contact = ContactRecord(**data)
        self.user1.contact_book.update(email, updated_contact)
        return {"message": "Contact updated successfully"}

    def DELETE(self, email):
        self.user1.contact_book.delete(email)
        return {"message": "Contact deleted successfully"}


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount(ContactBookAPI, '/contacts', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()