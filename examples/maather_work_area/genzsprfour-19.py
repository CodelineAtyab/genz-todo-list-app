import cherrypy
import os


class Root(object):
    @cherrypy.expose()
    def index(self):
        pass
class ContactRecordsV1(object):
    exposed = True

    def GET(self, phone_number):
        return f"Handled READ request with this phone number: {phone_number}"


    @cherrypy.tools.json_in()
    def POST(self, *args, **kwargs):
        return f"Handled CREATE request with this data: {cherrypy.request.json}"

    @cherrypy.tools.json_in()
    def PUT(self, phone_number):
        return f"Handled UPDATE request with this data: {cherrypy.request.json}"


    def DELETE(self, phone_number):
        return f"Handled REMOVE request with this data: {phone_number}"


cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})

# Mount the ContactsAPI application
cherrypy.tree.mount(ContactRecordsV1(), '/api/v1/contacts', {
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