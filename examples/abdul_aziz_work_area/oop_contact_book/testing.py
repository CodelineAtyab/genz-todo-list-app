import unittest
import requests

class TestGetContactAPI(unittest.TestCase):
    def test_get_contact(self):
        url = 'http://127.0.0.1:8080/api/contacts?name=John%20Doe'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', response.json()['contacts'])

if __name__ == '__main__':
    unittest.main()
