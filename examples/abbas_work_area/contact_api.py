import cherrypy
import json
import os

import contact_services
from OOP_contact import ContactBook
from OOP_contact_record import ContactRecord


class ContactRecordsV1(object):
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, add_contact=None):
        contact_book = ContactBook()
        res_msg = {"status": "FAIL", "data": []}
        if add_contact:
            filtered_contact_rec = contact_book.read_contact(add_contact)
            res_msg = {"status": "SUCCESS", "data": filtered_contact_rec}
        else:
            res_msg = {"status": "SUCCESS",
                       "data": contact_book.open_write_file()}
        return res_msg

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, *args, **kwargs):
        contact_book = ContactBook()
        res_msg = {"status": "FAIL", "data": None}
        inc_name = cherrypy.request.json["add_name"]
        inc_contact = cherrypy.request.json["add_contact"]
        inc_email = cherrypy.request.json["add_email"]
        inc_address = cherrypy.request.json["add_address"]

        new_contact_rec_dict = ContactRecord(add_name=inc_name,
                                             add_contact=inc_contact,
                                             add_email=inc_email,
                                             add_address=inc_address).__dict__

        csv_data = ','.join(map(str, [new_contact_rec_dict[field] for field in
                                      ['add_name', 'add_contact', 'add_email', 'add_address']]))

        contact_book.open_write_file(csv_data + "\n", "a")
        res_msg["status"] = "SUCCESS"
        res_msg["data"] = new_contact_rec_dict
        return res_msg

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, add_contact):
        res_msg = {"status": "FAIL", "data": ""}
        contact_book = ContactBook()
        old_info = add_contact
        filtered_contact_rec = contact_book.read_contact(old_info)

        try:
            contact_key = ["add_name", "add_contact", "add_email", "add_address"]
            contact_values = filtered_contact_rec.split(",")
            contact_dict = dict(zip(contact_key, contact_values))

            json_input = cherrypy.request.json
            for key in contact_key:
                if key in json_input:
                    contact_dict[key] = json_input[key]

            contact_book.update_contact(old_info, contact_dict["add_name"], contact_dict["add_contact"],
                                        contact_dict["add_email"], contact_dict["add_address"])

            res_msg = {"status": "SUCCESS", "data": contact_dict}

        except Exception as ex:
            res_msg = {"status": "FAIL", "data": str(ex)}

        return res_msg

    @cherrypy.tools.json_out()
    def DELETE(self, add_contact):
        contact_book = ContactBook()
        res_msg = {"status": "FAIL", "data": []}
        try:
            contact_book.delete_contact(add_contact)
            res_msg = {"status": "SUCCESS", "data": []}
        except Exception as ex:
            res_msg = {"status": "FAIL", "data": str(ex)}

        return res_msg

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PATCH(self, format_choice):
        contact_book = ContactBook()
        res_msg = {"status": "FAIL", "data": []}

        try:
            if format_choice == '1':
                new_format = 'csv'
            elif format_choice == '2':
                new_format = 'txt'
            elif format_choice == '3':
                new_format = 'json'
            else:
                print("Invalid choice, defaulting to CSV format.")
                new_format = 'csv'

            contact_book.load_contacts(new_format)
            res_msg = {"status": "SUCCESS", "data": new_format}

        except Exception as ex:
            res_msg = {"status": "FAIL", "data": str(ex)}

        return res_msg



