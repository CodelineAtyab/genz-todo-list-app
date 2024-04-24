import cherrypy
from cherrypy.test import helper

from examples.abdul_aziz_work_area.oop_contact_book.mainapi import ContactBookAPI


class TestApp(helper.CPWebCase):
    def setup_server(self):
        cherrypy.tree.mount(ContactBookAPI(), '/api/contacts', {'/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }})

    def test_post_contact(self):
        self.getPage("/api/contacts", method='POST', body='{"name": "John Doe", "phone": "123-456-7890", "email": "john.doe@example.com", "address": "123 Elm St"}', headers=[('Content-Type', 'application/json')])
        self.assertStatus('200 OK')
        self.assertInBody('Contact with phone number 123-456-7890 created')

if __name__ == '__main__':
    import unittest
    unittest.main()
