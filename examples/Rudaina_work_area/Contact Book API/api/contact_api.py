import cherrypy
from models.contact_record import ContactRecord
from models.contact_book_service import ContactBookService

class ContactAPI:
    exposed = True

    def __init__(self):
        self.contact_book_service = ContactBookService()

    @cherrypy.tools.json_out()
    def GET(self, email=None):
        if email:
            contact = self.contact_book_service.search_contact(email)
            if contact:
                return contact.to_dict()
            else:
                raise cherrypy.HTTPError(404, "Contact not found")
        else:
            return [contact.to_dict() for contact in self.contact_book_service.contact_book.contacts]

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        data = cherrypy.request.json
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')
        address = data.get('address')
        if not (name and phone and email and address):
            raise cherrypy.HTTPError(400, "Invalid request parameters")
        self.contact_book_service.add_contact(name, phone, email, address)
        return {"message": "Contact added successfully"}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, email):
        data = cherrypy.request.json
        updated_contact = ContactRecord(**data)
        if not self.contact_book_service.update_contact(email, updated_contact):
            raise cherrypy.HTTPError(404, "Contact not found")
        return {"message": "Contact updated successfully"}

    def DELETE(self, email):
        if not self.contact_book_service.delete_contact(email):
            raise cherrypy.HTTPError(404, "Contact not found")
        return {"message": "Contact deleted successfully"}


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount(ContactAPI(), '/contacts', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
