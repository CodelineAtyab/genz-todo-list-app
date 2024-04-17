import cherrypy
from service.contact_record import ContactRecord
from service.app_user import AppUser


class ContactBookAPI:
    @cherrypy.tools.json_out()
    def GET(self, email=None):
        if email:
            contact = self.user.contact_book.search(email)
            if contact:
                return contact.__dict__
            else:
                raise cherrypy.HTTPError(404, "Contact not found")
        else:
            return [contact.__dict__ for contact in self.user.contact_book.contacts]

    @cherrypy.tools.json_in()
    def POST(self):
        data = cherrypy.request.json
        contact = ContactRecord(**data)
        self.user.contact_book.add(contact)
        return {"message": "Contact added successfully"}

    @cherrypy.tools.json_in()
    def PUT(self, email):
        data = cherrypy.request.json
        updated_contact = ContactRecord(**data)
        self.user.contact_book.update(email, updated_contact)
        return {"message": "Contact updated successfully"}

    def DELETE(self, email):
        self.user.contact_book.delete(email)
        return {"message": "Contact deleted successfully"}

if __name__ == '__main__':
    def create_user(username, email, phone):
        return AppUser(username, email, phone)

    def create_contact_book_api(username, email, phone):
        contact_book_api = ContactBookAPI()
        contact_book_api.user = create_user(username, email, phone)
        return contact_book_api

    # Define the URL mapping for the CherryPy API
    class Root:
        @cherrypy.expose
        def contacts(self, username=None, email=None, phone=None):
            if username and email and phone:
                contact_book_api = create_contact_book_api(username, email, phone)
                cherrypy.tree.mount(contact_book_api, '/')
                return "ContactBookAPI mounted successfully"
            else:
                return "Please provide username, email, and phone in the URL parameters"

    # Configure CherryPy server
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})


cherrypy.engine.start()
cherrypy.engine.block()
