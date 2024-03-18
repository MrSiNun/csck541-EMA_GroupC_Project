import unittest
from cryptography.fernet import Fernet
import encryption_final

class TestEncryptionFinal(unittest.TestCase):

    def test_generate_encryption_key(self):
        key = encryption_final.generate_encryption_key()
        self.assertIsInstance(key, bytes)

    def test_save_encryption_key(self):
        key = Fernet.generate_key()
        encryption_final.save_encryption_key(key)
        # Add assertions to check if the key is saved to the file correctly

    # You can also write a test for the main function if it has any side effects

if __name__ == '__main__':
    unittest.main()