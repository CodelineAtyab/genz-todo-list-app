import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "<h1>Welcome to the GenZ team Ms A and Ms B</h1>"


cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(HelloWorld())