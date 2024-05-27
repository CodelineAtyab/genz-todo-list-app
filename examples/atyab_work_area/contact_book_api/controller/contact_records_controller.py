import cherrypy

import cbms.contact_book_service as contact_book_service_instance
from cbms.contact_record import ContactRecord


class ContactRecordsV1(object):
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, measurement=None):
        res_msg = {"status": "SUCCESS", "err_msg": "", "result": [2, 7, 7]}
        return res_msg


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, *args, **kwargs):
        res_msg = {"status": "FAIL", "data": None}
        inc_phone_number = cherrypy.request.json["phone_number"]
        inc_name = cherrypy.request.json["name"]
        inc_email = cherrypy.request.json["email"]

        new_contact_rec_dict = ContactRecord(phone_number=inc_phone_number,
                                             name=inc_name,
                                             email=inc_email).__dict__

        contact_book_service_instance.contact_book.contact_records.append(new_contact_rec_dict)
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

