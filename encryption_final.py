from cryptography.fernet import Fernet

def generate_encryption_key():
    """
    Generates a new encryption key using Fernet.
    """
    return Fernet.generate_key()


def save_encryption_key(key):
    """
    Saves the generated encryption key to a file.

    Args:
    - key: The encryption key to be saved.
    """
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)


def main():
    """
    Main function to generate and save an encryption key.
    """
    encryption_key = generate_encryption_key()
    save_encryption_key(encryption_key)
    print("A new encryption key has been generated and saved.")


if __name__ == "__main__":
    main()