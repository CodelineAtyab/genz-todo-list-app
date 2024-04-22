import unittest

from models.item import Item


class TestTodoItemValidation(unittest.TestCase):
    def test_valid_item(self):
        test_item = Item("Milk", "pending")
        self.assertTrue(test_item.is_valid())

    def test_empty_description(self):
        item = Item("", "completed")
        self.assertFalse(item.is_valid())

    def test_unsupported_status(self):
        item = Item("Go to gym", "done")
        self.assertFalse(item.is_valid())

    def test_non_string_description(self):
        item = Item(1234, "pending")
        self.assertFalse(item.is_valid())

    def test_missing_status(self):
        item = Item("Walk the dog", "")
        self.assertFalse(item.is_valid())


if __name__ == '__main__':
    unittest.main()

