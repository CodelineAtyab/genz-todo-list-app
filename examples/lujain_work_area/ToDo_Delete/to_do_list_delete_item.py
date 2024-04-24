import cherrypy
from TodoList import TodoList
from Item import Item

class TodoListAPI:

    def __init__(self):
        self.todo_list = TodoList()
        self.todo_list.if_header_exists()
        # Adding initial items
        self.todo_list.append_item(Item("Buy groceries", "pending"))
        self.todo_list.append_item(Item("Complete homework", "completed"))
        self.todo_list.append_item(Item("Complete homewoddddrk", "pending"))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def delete_todo_item(self, description=None, status=None):
        try:
            if description:
                deleted_items = [item for item in self.todo_list.items if item.description == description]
                self.todo_list.items = [item for item in self.todo_list.items if item.description != description]
            elif status:
                deleted_items = [item for item in self.todo_list.items if item.status == status]
                self.todo_list.items = [item for item in self.todo_list.items if item.status != status]
            else:
                cherrypy.response.status = 400
                return {"Error": "Neither description nor status provided for deletion"}

            if not deleted_items:
                cherrypy.response.status = 404
                return {"Error": "No matching items found for deletion"}

            self.todo_list.save_items()
            # cherrypy.response.status = 204
            return {"Message": f"{len(deleted_items)} item(s) deleted successfully"}

        except Exception as e:
            cherrypy.response.status = 500
            return {"error": str(e)}

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})  # Allow access from any IP
    cherrypy.config.update({'server.socket_port': 8080})  # Specify the port
    cherrypy.quickstart(TodoListAPI())
