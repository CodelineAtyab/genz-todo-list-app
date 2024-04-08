import unittest
from verify import verify_email


class ValidateTest(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(verify_email("test@example.com"))

    def test_invalid_missingtld(self):
        assert verify_email("test@example") == False

    def test_valid_sub(self):
        assert verify_email("test@sub.example.com") == True

    def test_invalid_char(self):
        assert verify_email("test!example.com") == False

    def test_invalid_missing_symbol(self):
        assert verify_email("testexample.com") == False

if __name__ == "__main__":
    unittest.main(verbosity=2)
