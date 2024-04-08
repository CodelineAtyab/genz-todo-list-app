import unittest
from email_validation import validate_email


class TestContactBook(unittest.TestCase):
    def test_invalid_email_with_consecutive_dots(self):
        """Test validation of email if consecutive dots are found."""
        email = "test..example.com"
        self.assertFalse(validate_email(email))

    def test_invalid_email_with_forbidden_characters(self):
        """Test validation for all special characters we do not support in an email address."""
        email = "test&example.com"
        self.assertFalse(validate_email(email))

    def test_valid_email_with_unusual_top_level_domain(self):
        """Test validation of email with a top-level domain that isn't common."""
        email = "test@example.co.rip"
        self.assertTrue(validate_email(email))

    def test_valid_email_with_plus_tag(self):
        """Test validation of email with a plus tag."""
        email = "test+tag@example.com"
        self.assertTrue(validate_email(email))

    def test_invalid_email_with_missing_local_part(self):
        """Test validation of email if the local part is missing."""
        email = "@example.com"
        self.assertFalse(validate_email(email))

    def test_invalid_email_with_trailing_dot(self):
        """Test validation of email with trailing dot in the local part of the email."""
        email = "test.@example.com"
        self.assertFalse(validate_email(email))
        print((validate_email(email)))

if __name__ == "__main__":
    unittest.main(verbosity=2)