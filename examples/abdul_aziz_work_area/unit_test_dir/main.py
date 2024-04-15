import unittest
from email_validity import validate_email


class ValidateTest(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(validate_email("test@example.com"))

    def test_invalid_missingtld(self):
        assert validate_email("test@example") == False

    def test_valid_sub(self):
        assert validate_email("test@sub.example.com") == True

    def test_invalid_char(self):
        assert validate_email("test!example.com") == False

    def test_invalid_missing_symbol(self):
        assert validate_email("testexample.com") == False

if __name__ == "__main__":
    unittest.main(verbosity=3)
