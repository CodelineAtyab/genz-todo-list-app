import cherrypy

from service.contact_records_service import data_store_dict


class ContactRecordsV1(object):
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, phone_number=None):
        res_msg = {"status": "FAIL", "data": ""}
        if not phone_number:
            res_msg["data"] = data_store_dict
            res_msg["status"] = "SUCCESS"
        else:
            try:
                res_msg["data"] = data_store_dict[phone_number]
                res_msg["status"] = "SUCCESS"
            except Exception:
                res_msg["error"] = "Unable to fetch the record."

        return res_msg


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, *args, **kwargs):
        res_msg = {"status": "FAIL", "data": ""}
        try:
            req_data_dict = cherrypy.request.json
            data_store_dict[req_data_dict["phone_number"]] = {"name": req_data_dict["name"],
                                                              "email": req_data_dict["email"]}
            res_msg["status"] = "SUCCESS"
        except Exception:
            res_msg["error"] = "Unable to create the record."

        return res_msg

    @cherrypy.tools.json_in()
    def PUT(self, phone_number="00000000"):
        return f"Handled UPDATE request with this data: {cherrypy.request.json}"


    def DELETE(self, phone_number="00000000"):
        return f"Handled REMOVE request with this data: {phone_number}"

