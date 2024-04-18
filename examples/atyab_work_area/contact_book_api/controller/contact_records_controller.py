import cherrypy

import cbms.contact_book_service as contact_book_service_instance


class ContactRecordsV1(object):
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, phone_number=None):
        res_msg = {"status": "FAIL", "data": [rec.__dict__ for rec in contact_book_service_instance.contact_book.contact_records]}
        return res_msg


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, *args, **kwargs):
        res_msg = {"status": "FAIL", "data": ""}
        return res_msg

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, phone_number="00000000"):
        res_msg = {"status": "FAIL", "data": ""}
        return res_msg

    @cherrypy.tools.json_out()
    def DELETE(self, phone_number="00000000"):
        res_msg = {"status": "FAIL", "data": ""}
        return res_msg

