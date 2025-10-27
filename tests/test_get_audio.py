import unittest

from src.Audio_File import Audio_File, get_Audio_Files_list
from src.get_data import get_data_from_csv
from config.config import BUILD_AUDIO_FILES_PATH
class TestAudio(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(Exception):
            _ = get_Audio_Files_list([])

    def test_valid_list(self):
        result = get_data_from_csv("tests/fixtures/test.csv")
        example_list = [row[2] for row in result]
        audio_files = get_Audio_Files_list(example_list, BUILD_AUDIO_FILES_PATH)
        self.assertEqual(len(audio_files), 2)

if __name__ == "__main__":
    unittest.main()