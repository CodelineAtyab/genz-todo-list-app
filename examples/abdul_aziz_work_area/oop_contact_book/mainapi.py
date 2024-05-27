import cherrypy
from contact_book import ContactBook, JsonContactBook, CsvContactBook
from contact_record import ContactRecord

class ContactBookAPI(object):
    exposed = True

    def __init__(self):
        # Decide the format or take from a config setting
        self.contact_book = JsonContactBook()

    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def POST(self):
        input_json = cherrypy.request.json
        contact = ContactRecord(name=input_json["name"], phone_number=input_json["phone"], email=input_json["email"], address=input_json.get("address", ""))
        self.contact_book.add_contact(contact)
        return {"status": "success", "message": f"Contact with phone number {input_json['phone']} created."}

    def DELETE(self, contactId):
        # Implement contact deletion logic here
        return {"status": "success", "message": "Contact deleted."}

    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def PUT(self, contactId):
        input_json = cherrypy.request.json
        # Update contact logic here
        return {"status": "success", "message": "Contact updated."}

    @cherrypy.tools.json_out()
    def GET(self, **params):
        if 'name' in params:
            contacts = self.contact_book.find_contact(params['name'])
            # Convert each contact record to a dictionary
            return {"status": "success", "contacts": [contact.to_dict() for contact in contacts]}
        else:
            return {"status": "error", "message": "Name parameter is required"}


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
