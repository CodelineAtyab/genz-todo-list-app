import unittest
from email_validator import validate_email

class TestValidate(unittest.TestCase):
    def test_valid_email_standard_format():
        assert validate_email("test@example.com") == True

    def test_valid_email_subdomain():
        assert validate_email("test@sub.example.com") == True

    def test_valid_email_unusual_tld():
        assert validate_email("test@example.co.in") == True

    def test_valid_email_plus_tag():
        assert validate_email("test+tag@example.com") == True

    def test_invalid_email_missing_at_symbol():
        assert validate_email("testexample.com") == False

    def test_invalid_email_missing_tld():
        assert validate_email("test@example") == False

    def test_invalid_email_invalid_characters():
        assert validate_email("test!example.com") == False

    def test_invalid_email_empty_string():
        assert validate_email("") == False

    def test_invalid_email_whitespace_only():
        assert validate_email("   ") == False

if __name__ == "__main__":
    unittest.main(verbosity=2)