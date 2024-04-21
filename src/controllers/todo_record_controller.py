import cherrypy

from src.services import todo_list_services
from src.models.todolist import TodoList


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
        # Open the file and read everything using readlines()
        list_of_lines_in_file = TodoList.open_write_file()
        
        def create_list_of_dictionaries(data_values):
            list_of_dicts = []
            for item in data_values:
                item_data = item.split(",")
                new_dict = {"description": item_data[0], "status": item_data[1]}
                list_of_dicts.append(new_dict)
            return list_of_dicts
        
        # If task list is empty
        if len(list_of_lines_in_file) < 2: 
            res_msg = {"status": "SUCCESS", "data": "EMPTY LIST"}
        # GET request all items
        elif record_id == None: 
            res_msg = {"status": "SUCCESS", "data": create_list_of_dictionaries(list_of_lines_in_file[1:])}
        # GET request one item
        else:
            found_items = []
            # Search for the item in task list
            for item in list_of_lines_in_file:
                item_data = item.split(",")
                if item_data[0] == record_id:
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
