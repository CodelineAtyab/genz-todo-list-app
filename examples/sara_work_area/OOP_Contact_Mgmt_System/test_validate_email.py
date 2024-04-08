import unittest
from contact_record import ContactRecord
from utils import validate_email


class TestValidateEmail(unittest.TestCase):

    def test_valid_email(self):
        valid_email = "sara@example.com"
        self.assertTrue(validate_email(valid_email))

    def test_email_multiple_subdomains(self):
        invalid_email = "sara@sub.example.com"
        self.assertTrue(validate_email(invalid_email))

    def test_email_no_sign(self):
        invalid_email = "saraexample.com"
        self.assertFalse(validate_email(invalid_email))

    def test_email_no_dot(self):
        invalid_email = "sara@examplecom"
        self.assertFalse(validate_email(invalid_email))

    def test_email_no_tld(self):
        invalid_email = "sara@example."
        self.assertFalse(validate_email(invalid_email))

    def test_email_invalid_char(self):
        invalid_email = "sara!example.com"
        self.assertFalse(validate_email(invalid_email))


if __name__ == "__main__":
    unittest.main(verbosity=2)
