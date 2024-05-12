import cherrypy

import contact_book_service as contact_book_service_instance
from contact_record import ContactRecord
from CRUD_record import CRUDRecord
from app_user import AppUser
from csv_contact_book import CsvContactBook


class ContactRecordsV1(object):
    exposed = True

    def __init__(self):
        self.user = AppUser(123, "sara")
        self.contact_book = CsvContactBook(self.user.get_phone_number())

    @cherrypy.tools.json_out()
    def GET(self, phone_number=None):
        res_msg = {"status": "FAIL", "data": []}
        if phone_number:
            for rec in contact_book_service_instance.contact_book.contact_records:
                if rec.phone_num == phone_number:
                    res_msg = {"status": "PASS", "data": rec.__dict__}
        else:
            res_msg = {"status": "SUCCESS",
                       "data": contact_book_service_instance.contact_book.contact_records}

        return res_msg

    # @cherrypy.tools.json_in()
    # @cherrypy.tools.json_out()
    # def GET(self, phone_number=None):
    #     res_msg = {"status": "FAIL", "data": []}
    #     print("in get")
    #     if phone_number:
    #         result = CRUDRecord.search_record(phone_number)
    #         res_msg = {"status": "PASS", "data": result.__dict__}
    #     else:
    #         res_msg = {"status": "SUCCESS",
    #                    "data": contact_book_service_instance.contact_book.contact_records}
    #
    #     return res_msg

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, *args, **kwargs):
        res_msg = {"status": "FAIL", "data": None}
        inc_phone_number = cherrypy.request.json["phone_number"]
        inc_name = cherrypy.request.json["name"]
        inc_email = cherrypy.request.json["email"]
        inc_address = cherrypy.request.json["address"]

        new_contact_rec_dict = ContactRecord(phone_number=inc_phone_number,
                                             name=inc_name,
                                             email=inc_email,
                                             address=inc_address).__dict__

        contact_book_service_instance.contact_book.contact_records.append(new_contact_rec_dict)
        self.contact_book.store_contact(ContactRecord(phone_number=inc_phone_number,
                                                      name=inc_name,
                                                      email=inc_email,
                                                      address=inc_address))
        res_msg["status"] = "SUCCESS"
        res_msg["data"] = new_contact_rec_dict
        return res_msg

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, phone_number):
        res_msg = {"status": "FAIL", "data": ""}
        filtered_contact_rec = list(filter(lambda rec: rec["phone_num"] == phone_number,
                                           contact_book_service_instance.contact_book.contact_records))[0]

        filtered_contact_rec["name"] = cherrypy.request.json["name"]
        filtered_contact_rec["email"] = cherrypy.request.json["email"]

        res_msg = {"status": "SUCCESS", "data": filtered_contact_rec}

        return res_msg

    @cherrypy.tools.json_out()
    def DELETE(self, phone_number):
        res_msg = {"status": "SUCCESS"}
        filtered_contact_rec = list(filter(lambda rec: rec["phone_num"] == phone_number,
                                           contact_book_service_instance.contact_book.contact_records))[0]

        contact_book_service_instance.contact_book.contact_records.remove(filtered_contact_rec)
        return res_msg

