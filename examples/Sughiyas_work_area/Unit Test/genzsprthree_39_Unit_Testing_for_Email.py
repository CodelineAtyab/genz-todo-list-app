import unittest
from email_validator import validate_email

class TestValidate(unittest.TestCase):
    def test_valid_email_standard_format(self):
        assert validate_email("test@example.com") == True

    def test_valid_email_subdomain(self):
        assert validate_email("test@sub.example.com") == True

    def test_valid_email_unusual_tld(self):
        assert validate_email("test@example.co.in") == True

    def test_valid_email_plus_tag(self):
        assert validate_email("test+tag@example.com") == True

    def test_invalid_email_missing_at_symbol(self):
        assert validate_email("testexample.com") == False

    def test_invalid_email_missing_tld(self):
        assert validate_email("test@example") == False

    def test_invalid_email_invalid_characters(self):
        assert validate_email("test!example.com") == False

    def test_invalid_email_empty_string(self):
        assert validate_email("") == False

    def test_invalid_email_whitespace_only(self):
        assert validate_email("   ") == False

if __name__ == "__main__":
    unittest.main(verbosity=2)