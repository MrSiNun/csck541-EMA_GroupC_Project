import unittest
import client_final
from cryptography.fernet import Fernet

class TestClientFinal(unittest.TestCase):

    def test_load_encryption_key(self):
        key = client_final.load_encryption_key()
        self.assertIsInstance(key, bytes)

    def test_clean_and_format_name(self):
        formatted_name = client_final.clean_and_format_name("  john  ")
        self.assertEqual(formatted_name, "John")

    def test_collect_user_data(self):
        # You can use unittest.mock to mock the input function and test the output
        pass

    def test_choose_format(self):
        # You can use unittest.mock to mock the input function and test the output
        pass

    def test_validate_continuation_response(self):
        # You can use unittest.mock to mock the input function and test the output
        pass

    def test_serialize_data(self):
        data = {"first_name": "John", "last_name": "Doe"}
        serialized_json = client_final.serialize_data(data, "json")
        serialized_binary = client_final.serialize_data(data, "binary")
        serialized_xml = client_final.serialize_data(data, "xml")
        # Add assertions to check the serialized data

    # You can also write a test for the main function if it has any side effects

if __name__ == '__main__':
    unittest.main()