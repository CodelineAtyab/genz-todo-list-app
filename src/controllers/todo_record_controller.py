import cherrypy

from src.services import todo_list_services
from src.models.todolist import TodoList


class TodoRecordsV1(object):
    exposed = True


    @cherrypy.tools.json_out()
    def GET(self, description: str=None):
        """
        Handles the GET request and return a JSON response.
        :param record_id: Id of a specific todo record resource.
        :return: All the records if id is None, otherwise a specific record if there is an id.
        Dict will be converted to JSON automatically due to the json_out decorator.
        """
        # Generates the data for the response
        def create_list_of_dictionaries(data_values):
            list_of_dicts = []
            for item in data_values:
                new_dict = {"description": item.description, "status": item.status}
                list_of_dicts.append(new_dict)
            return list_of_dicts
        
        # If task list is empty
        if len(todo_list_services.list_of_lines_in_file) < 2: 
            res_msg = {"status": "SUCCESS", "data": []}
        # GET request all items
        elif description == None: 
            res_msg = {"status": "SUCCESS", "data": create_list_of_dictionaries(todo_list_services.todo_list.items[1:])}
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
