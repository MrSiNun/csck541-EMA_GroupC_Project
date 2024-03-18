import unittest
import server_final
from cryptography.fernet import Fernet

class TestServerFinal(unittest.TestCase):

    def test_load_encryption_key(self):
        key = server_final.load_encryption_key()
        self.assertIsInstance(key, bytes)

    def test_deserialize_data(self):
        key = server_final.load_encryption_key()  # Load the encryption key
        cipher = Fernet(key)  # Create a Fernet object using the encryption key
        encrypted_data = cipher.encrypt(b'test_data')
        format_detected, deserialized_data = server_final.deserialize_data(encrypted_data, cipher)
        self.assertIn(format_detected, ["binary", "json", "xml", "session_end", "unknown"])
        if format_detected == "binary":
            self.assertEqual(deserialized_data, b'test_data')
        elif format_detected == "json":
            self.assertIsInstance(deserialized_data, dict)
        elif format_detected == "xml":
            self.assertIsInstance(deserialized_data, dict)
        elif format_detected == "session_end":
            self.assertIsNone(deserialized_data)
        else:
            self.assertIsInstance(deserialized_data, str)

    # You can also write a test for the main function if it has any side effects

if __name__ == '__main__':
    unittest.main()