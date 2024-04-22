import cherrypy

from src.models.item import Item
from src.services import todo_list_services
from src.services.todo_list_services import todo_list


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
        # Extract data from JSON payload
        input_data = cherrypy.request.json
        description = input_data.get('description')
        status = input_data.get('status', 'pending')  # Default to 'pending' if not provided

        # Input validation
        if not description:
            raise cherrypy.HTTPError(400, "Description is required")

        # Create a new todo item
        new_item = Item(description, status)
        todo_list.append_item(new_item)

        # Return the new item details and 201 Created status code
        cherrypy.response.status = 201
        return {"status": "success", "data": {"description": new_item.description, "status": new_item.status}}

    # Assuming the TodoList class has the method append_item that adds an item

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
