import unittest
import tempfile
import json
from library.json_converter import save_to_file, load_from_file


class TestJsonConverter(unittest.TestCase):
    def setUp(self):
        self.test_data = {'key': 'value'}
        self.temp_file = tempfile.NamedTemporaryFile()

    def test_save_to_file(self):
        save_to_file(self.test_data, self.temp_file.name)
        with open(self.temp_file.name, 'r') as file:
            content = json.load(file)
            self.assertIn('key', content)  # Checks if 'key' is one of the keys in the dictionary
            self.assertIn('value', content['key'])  # Checks if 'value' is one of the values in the dictionary
            self.assertEqual('value', content['key'])  # Checks if the value of 'key' is 'value'

    def test_load_from_file(self):
        # Ensure there is data in the temporary file
        self.test_save_to_file()
        data = load_from_file(self.temp_file.name)
        # Check if the loaded data matches the original data
        self.assertEqual(data, self.test_data)


if __name__ == '__main__':
    unittest.main()
