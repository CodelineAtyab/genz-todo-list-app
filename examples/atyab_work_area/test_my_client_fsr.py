import unittest
import responses

from my_client_fsr import fetch_profile


class ClientAppTest(unittest.TestCase):
    @responses.activate
    def test_profile_fetch_with_name(self):
        responses.add(responses.GET,
                      "https://api.github.com/users/codelineatyab",
                      json={"id": 12345, "name": "atyab"}, status=200)

        responses.add(responses.POST,
                      "https://api.github.com/users/codelineatyab",
                      json={"year": 2004, "msg": "POSTED Successfully!"}, status=200)

        status_1, res_dict_1 = fetch_profile("codelineatyab", method="GET")
        status_2, res_dict_2 = fetch_profile("codelineatyab", method="POST")

        self.assertEqual(200, status_1)
        self.assertIsInstance(res_dict_1, dict)
        self.assertTrue("id" in res_dict_1)
        self.assertEqual("atyab", res_dict_1["name"])

        self.assertEqual(200, status_2)
        self.assertIsInstance(res_dict_2, dict)
        self.assertTrue("msg" in res_dict_2)
        self.assertEqual("POSTED Successfully!", res_dict_2["msg"])

