import cherrypy
from cbm.app_user import AppUser
from cbm.contact_manager import ContactManager
from cbm.json_contact_book import JsonContactBook


class ContactBookApi:
    def __init__(self):
        self.contact_book = JsonContactBook
        self.user = AppUser("default", self.contact_book)
        self.manager = ContactManager(self.user)

    def update_file(self):
        self.manager.user.contact_book.store_contacts(
        list(self.manager.user.contact_book.contact_book_data_dict.values()))

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def add_contact(self):
        data = cherrypy.request.json
        keys = ["phone_number", "name", "email", "address"]
        if not all(key in data for key in keys):
            raise cherrypy.HTTPError(400, "invalid request")
        self.manager.add_contact(data)
        self.update_file()
        return "contact added successfully!"
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update_contact(self):
        data = cherrypy.request.json
        keys = ["phone_number", "attribute", "value"]
        if not all(key in data for key in keys):
            raise cherrypy.HTTPError(400, "invalid request")
        self.manager.update_contact(data["phone_number"], data["attribute"], data["value"])
        self.update_file()
        return "contact updated successfully."
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def delete_contact(self, phone_number):
        self.manager.delete_contact(phone_number)
        self.update_file()
        return "contact deleted successfully!"

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def search_contact(self, phone_number):
        contact = self.manager.search_contact(phone_number)
        return contact.to_dict() if contact else "contact not found."
    


if __name__ == "__main__":
    cherrypy.quickstart(ContactBookApi())
