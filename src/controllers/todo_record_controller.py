import cherrypy

from src.models.item import Item
from src.services import todo_list_services


class TodoRecordsV1(object):
    exposed = True


    @cherrypy.tools.json_out()
    def GET(self, description: str = ""):
        """
        Handles the GET request and return a JSON response.
        :param description: Description of a specific todo record resource.
        :return: All the records if id is None, otherwise a specific record if there is an id.
        Dict will be converted to JSON automatically due to the json_out decorator.
        """
        res_msg = {"status": "FAIL", "data": []}

        # Generates the data for the response
        def create_list_of_dictionaries(data_values):
            list_of_dicts = []
            for item in data_values:
                new_dict = {"description": item.description, "status": item.status}
                list_of_dicts.append(new_dict)
            return list_of_dicts

        # GET request all items
        if not description:
            res_msg["status"] = "SUCCESS"
            res_msg["data"] = create_list_of_dictionaries(todo_list_services.todo_list.items[1:])

        # GET request one item
        else:
            found_items = []
            # Search for the item in task list
            for item in todo_list_services.todo_list.items:
                if item.description.lower() == description.lower():
                    found_items.append(item)
            # If item is found in task list
            if found_items:
                res_msg = {"status": "SUCCESS", "data": create_list_of_dictionaries(found_items)}
            else: 
                res_msg = {"status": "FAIL", "data": "NOT FOUND"}
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

        # Extract data from JSON payload
        input_data = cherrypy.request.json
        description = input_data.get('description')
        status = input_data.get('status', 'pending')  # Default to 'pending' if not provided

        # Input validation
        if not description:
            raise cherrypy.HTTPError(400, "Description is required")

        # Create a new todo item
        new_item = Item(description, status)
        todo_list_services.todo_list.append_item(new_item)

        # Return the new item details and 201 Created status code
        cherrypy.response.status = 201
        res_msg["status"] = "success"
        res_msg["data"] = {"description": new_item.description, "status": new_item.status}
        return res_msg

    # Assuming the TodoList class has the method append_item that adds an item

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
        for item in todo_list_services.todo_list.items:
            if item.description.strip().lower() == todo_description.strip().lower():
                found_item = item

        if found_item:
            item_to_update = todo_list_services.Item(description=found_item.description,
                                                     status=found_item.status)
            if 'description' in request_data:
                item_to_update.description = request_data['description']
            if 'status' in request_data:
                item_to_update.status = request_data['status']

        updated = todo_list_services.todo_list.replace_item(found_item, item_to_update)

        if updated:
            res_msg['status'] = 'SUCCESS'
            res_msg['data'] = 'UPDATED'
        else:
            cherrypy.response.status = 404  # Not Found
            res_msg['data'] = 'Item not found.'
        return res_msg


    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def DELETE(self, description=None, status=None):
        """
        Handles the DELETE request and returns a JSON response.
        :param record_id: Id of a specific todo record resource.
        :return: The status, if the operation is successful or not, along with the record that is deleted.
        """
        res_msg = {"status": "FAIL", "data": []}
        try:
            items_to_delete = []
            if description:
                items_to_delete = [item for item in todo_list_services.todo_list.items if item.description == description]
                for item_to_delete in items_to_delete:
                    todo_list_services.todo_list.items.remove(item_to_delete)
            elif status:
                items_to_delete = [item for item in todo_list_services.todo_list.items if item.status == status]
                for item_to_delete in items_to_delete:
                    todo_list_services.todo_list.items.remove(item_to_delete)
            else:
                cherrypy.response.status = 400
                return {"Error": "Neither description nor status provided for deletion"}

            if not items_to_delete:
                cherrypy.response.status = 404
                return {"Error": "No matching items found for deletion"}

            todo_list_services.todo_list.save_items()
            if items_to_delete:
                res_msg['status'] = 'SUCCESS'

            return res_msg
        except Exception as e:
            cherrypy.response.status = 500
            return {"error": str(e)}
