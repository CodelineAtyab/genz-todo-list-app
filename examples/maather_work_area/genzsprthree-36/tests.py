import unittest
from validate_email import validate_email


class TestValidateEmail(unittest.TestCase):

    def test_valid_standard_email(self):
        assert validate_email("test@example.com") == True

    def test_valid_subdomain_email(self):
        assert validate_email("test@sub.example.com") == True

    def test_valid_plus_tag_email(self):
        assert validate_email("test+tag@example.com") == True

    def test_valid_unusual_tld_email(self):
        assert validate_email("test@example.tld") == True

    def test_invalid_missing_tld_email(self):
        assert validate_email("test@example") == False

    def test_invalid_forbidden_characters_email(self):
        assert validate_email("test!example.com") == False

    def test_invalid_missing_at_symbol_email(self):
        assert validate_email("example.com") == False


if __name__ == "__main__":
    unittest.main(verbosity=2)
