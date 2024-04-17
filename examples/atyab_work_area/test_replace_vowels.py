import unittest
from replace_vowels import replace_vowels_with


class TestReplaceVowels(unittest.TestCase):

    def setUp(self):
        print(self._testMethodDoc)
        super().setUp()
    def test_empty_word_with_dash(self):
        """
        test_empty_word_with_dash
        :return:
        """
        self.assertEqual(replace_vowels_with("", "-"), "")

    def test_a_string_with_space(self):
        """
        test_empty_word_with_dash
        :return:
        """
        self.assertEqual(replace_vowels_with("Hello World", " "), "Hll  W rld")

    def test_none_with_a_symbol(self):
        """
        test_empty_word_with_dash
        :return:
        """
        self.assertEqual(replace_vowels_with(None, "-"), "")

    def test_word_with_a_symbol_as_none(self):
        """
        test_empty_word_with_dash
        :return:
        """
        self.assertEqual(replace_vowels_with("Hello World", None), "Hello World")

    def test_none_with_a_symbol_as_none(self):
        """
        test_empty_word_with_dash
        :return:
        """
        self.assertEqual(replace_vowels_with(None, None), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
