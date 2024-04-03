import unittest
from replace_vowels import replace_vowels_with


class TestReplaceVowels(unittest.TestCase):
    def test_empty_word_with_dash(self):
        self.assertEqual(replace_vowels_with("", "-"), "")

    def test_a_string_with_space(self):
        self.assertEqual(replace_vowels_with("Hello World", " "), "H ll  W rld")

    def test_none_with_a_symbol(self):
        self.assertEqual(replace_vowels_with(None, "-"), "")

    def test_word_with_a_symbol_as_none(self):
        self.assertEqual(replace_vowels_with("Hello World", None), "Hello World")

    def test_none_with_a_symbol_as_none(self):
        self.assertEqual(replace_vowels_with(None, None), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
