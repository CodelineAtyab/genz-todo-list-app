import unittest

from conversion import Conversion


class TestConversion(unittest.TestCase):

    def test_string_with_double_letters(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('aa'), 'Result list: [1]')

    def test_string_multiple_letters(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('abbcc'), 'Result list: [2, 6]')

    def test_string_with_underscore(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('dz_a_aazzaaa'), 'Result list: [28, 53, 1]')

    def test_string_with_one_letter_underscore(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('a_'), 'Result list: [0]')

    def test_valid_string1(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('abcdabcdab'), 'Result list: [2, 7, 7]')

    def test_string_ending_with_underscore(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('abcdabcdab_'), 'Result list: [2, 7, 7, 0]')

    def test_string_starting_with_z(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('zdaaaaaaaabaaaaaaaabaaaaaaaabbaa'), 'Result list: [34]')

    def test_string_starting_with_double_z(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_'), 'Result list: [26]')

    def test_string_starting_with_z_a(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa'), 'Result list: [40, 1]')


if __name__ == "__main__":
    unittest.main(verbosity=2)
