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
        res_msg = {"status": "PASS", "data": [
            {"description": "some description one", "status": "pending"},
            {"description": "another description two", "status": "completed"}
        ]}
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
    def PUT(self, todo_description=None):
        """
        Handles the PUT request and returns a JSON response.
        :param todo_description: description of a specific todo record resource.
        :return: The status, if the operation is successful or not, along with the record that is updated.
        """

        res_msg = {"status": "FAIL", "data": ""}
        request_data = cherrypy.request.json
        found_item: todo_list_services.Item = None
        for item in todo_list_services.todo_list:
            if item.description.strip().lower() == todo_description.strip().lower():
                found_item = item

        if found_item:
            item_to_update = todo_list_services.Item(description=found_item.description,
                                                     status=found_item.status)
            if 'description' in request_data:
                item_to_update.description = request_data['description']
            if 'status' in request_data:
                item_to_update.description = request_data['Status']

        updated = todo_list_services.todo_list.replace_item(found_item, item_to_update)

        if updated:
            res_msg['status'] = 'SUCCESS'
            res_msg['data'] = item.__dict__
        else:
            cherrypy.response.status = 404  # Not Found
            res_msg['data'] = 'Item not found.'
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
