import cherrypy
import os
import sys


from src.controllers.todo_record_controller import TodoRecordsV1


class Root(object):
    @cherrypy.expose()
    def index(self):
        """
        This function is going to return index.html files present in the static directory.
        We don't need to implement it since it configured and cherrypy is going to handle it.
        """
        pass


SERVER_PORT = sys.argv[1] if sys.argv[1] else 8080
cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': int(SERVER_PORT)})

# Mount the ContactsAPI application
cherrypy.tree.mount(TodoRecordsV1(), '/api/v1/todoRecords', {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),  # Use method-based dispatching
        'tools.sessions.on': False,
        'tools.response_headers.on': True,
        'tools.response_headers.headers': [('Content-Type', 'text/plain')]
    }
})

cherrypy.tree.mount(Root(), '/', {
    '/': {
            'tools.staticdir.root': os.path.abspath(os.path.dirname(__file__)),
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'static',
            'tools.staticdir.index': 'index.html',
    }
})

# Start the CherryPy server
cherrypy.engine.start()
cherrypy.engine.block()
