import json
import cherrypy
from conversion import Conversion


class MeasurementConversion:
    exposed = True

    @cherrypy.tools.json_out()
    def __call__(self, user_input=None):
        res_msg = {"status": "SUCCESS", "data": ""}
        try:
            if not user_input:
                user_input = cherrypy.request.params.get('user_input')
            if user_input is not None:
                user_string = Conversion()
                res_msg["data"] = user_string.converted_string(user_input)
            else:
                res_msg["status"] = "ERROR"
                res_msg["data"] = "Missing user_input parameter"
        except Exception as e:
            res_msg["status"] = "ERROR"
            res_msg["data"] = str(e)
        return json.dumps(res_msg)


# Configure the server and start it
if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
    cherrypy.tree.mount(MeasurementConversion(), '/')
    cherrypy.engine.start()
    cherrypy.engine.block()
