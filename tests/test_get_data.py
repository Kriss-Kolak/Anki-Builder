import unittest

from src.get_data import get_data_from_csv

class TestGetData(unittest.TestCase):

    def test_basic_invalid_file(self):
        with self.assertRaises(Exception):
            result = get_data_from_csv("random_file")
    
    def test_basic_invalid_path(self):
        with self.assertRaises(Exception):
            result = get_data_from_csv("./source_decks")

if __name__ == "__main__":
    unittest.main()