import cherrypy

from src.services import todo_list_services


class TodoRecordsV1(object):
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, record_id=None):
        """
        Handles the GET request and return a JSON response.
        :param record_id: Id of a specific todo record resource.
        :return: All the records if id is None, otherwise a specific record if there is an id.
        Dict will be converted to JSON automatically due to the json_out decorator.
        """
        res_msg = {"status": "FAIL", "data": ""}
        return res_msg


    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        """
        Handles the POST request and returns a JSON response.
        The incoming raw JSON body would exist in cherrypy.request.json because of json_in decorator.
        :return: The status, if the operation is successful or not, along with the record that is created.
        """
        res_msg = {"status": "FAIL", "data": ""}
        return res_msg

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def PUT(self, record_id=None):
        """
        Handles the PUT request and returns a JSON response.
        :param record_id: Id of a specific todo record resource.
        :return: The status, if the operation is successful or not, along with the record that is updated.
        """
        res_msg = {"status": "FAIL", "data": ""}
        return res_msg

    @cherrypy.tools.json_out()
    def DELETE(self, record_id=None):
        """
        Handles the DELETE request and returns a JSON response.
        :param record_id: Id of a specific todo record resource.
        :return: The status, if the operation is successful or not, along with the record that is deleted.
        """
        res_msg = {"status": "FAIL", "data": ""}
        return res_msg
