import unittest


from email_verfication import verify_email


class AppTest(unittest.TestCase):
    def test_correct_email(self):
        self.assertTrue(verify_email("test@example.com"))

    def test_incorrect_email(self):
        self.assertFalse(verify_email("test@example"))

    def test_subdomain(self):
        self.assertTrue(verify_email("test@sub.example.com"))

    def test_invalidchar(self):
        self.assertFalse(verify_email("test!example.com"))

    def test_missingsymbol(self):
        self.assertFalse(verify_email("testexample.com"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
