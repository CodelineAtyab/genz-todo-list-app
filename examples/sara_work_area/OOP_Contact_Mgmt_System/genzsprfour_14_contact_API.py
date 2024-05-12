import cherrypy
from contact_record import ContactRecord
from app_user import AppUser
from csv_contact_book import CsvContactBook
from CRUD_record import CRUDRecord


class ContactAPI(object):
    exposed = True

    def __init__(self):
        self.user = AppUser(123, "sara")
        self.contact_book = CsvContactBook(self.user.get_phone_number())

    # @cherrypy.tools.json_in()
    # @cherrypy.tools.json_out()
    # def add_contact(self):
    #     try:
    #         data = cherrypy.request.json
    #         if all(key in data for key in ['name', 'phone_number', 'email', 'address']):
    #             contact = ContactRecord(data['phone_number'], data['name'], data['email'], data['address'])
    #             contact_book = CsvContactBook(self.user.get_phone_number())
    #             contact_book.store_contact(contact)
    #             return f"A new contact: {data['phone_number']} has been created successfully."
    #     except Exception as e:
    #         raise cherrypy.HTTPError(400, str(e))

    @cherrypy.tools.json_out()
    def search_contact(self, phone=None):
        if phone:
            results = CRUDRecord.search_record(phone)
        else:
            raise cherrypy.HTTPError(400, 'Invalid Request')

        return [contact.to_dict() for contact in results]


if __name__ == '__main__':
    cherrypy.quickstart(ContactAPI())
