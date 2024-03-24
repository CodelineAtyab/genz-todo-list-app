import cherrypy
from filing_crud.file_manager import store_row_in_file


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello from Atyab!"

    @cherrypy.expose
    def home(self, **kwargs):
        store_row_in_file(kwargs['joke'])
        return f"Joke stored successfully!"


cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
cherrypy.quickstart(HelloWorld())
