import socket
from cryptography.fernet import Fernet
import json
import pickle
import xml.etree.ElementTree as ET

def load_encryption_key():
    """Loads the encryption key from a file."""
    with open("encryption.key", "rb") as key_file:
        return key_file.read()

def clean_and_format_name(name):
    """Removes leading and trailing spaces and capitalizes the name."""
    return name.strip().capitalize()

def collect_user_data():
    """Collects user's first and last names with standardization."""
    first_name = clean_and_format_name(input("First Name: "))
    last_name = clean_and_format_name(input("Last Name: "))
    return {"first_name": first_name, "last_name": last_name}

def choose_format():
    """Allows the user to choose the data serialization format with input validation."""
    while True:
        format_choice = input("Choose format (json/binary/xml): ").lower().strip()
        if format_choice in ["json", "binary", "xml"]:
            return format_choice
        else:
            print("Invalid format choice. Please enter 'json', 'binary', or 'xml'.")

def validate_continuation_response():
    """Asks the user whether to continue and validates the response."""
    while True:
        response = input("Do you want to add more data? (yes/no): ").lower().strip()
        if response in ["yes", "no"]:
            return response
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

def serialize_data(data, format_choice):
    """Serializes data based on the chosen format."""
    if format_choice == "json":
        return json.dumps(data).encode()
    elif format_choice == "binary":
        return pickle.dumps(data)
    elif format_choice == "xml":
        root = ET.Element("data")
        for key, value in data.items():
            ET.SubElement(root, key).text = value
        return ET.tostring(root, encoding='utf8', method='xml')

def main():
    encryption_key = load_encryption_key()
    cipher = Fernet(encryption_key)
    
    HOST, PORT = 'localhost', 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Connected to the server.")

        while True:
            data = collect_user_data()
            format_choice = choose_format()
            serialized_data = serialize_data(data, format_choice)
            encrypted_data = cipher.encrypt(serialized_data)
            client_socket.sendall(encrypted_data)
            print("Encrypted and serialized data sent successfully.")

            more_data = validate_continuation_response()
            if more_data != 'yes':
                print("Sending session end signal to server.")
                client_socket.sendall(cipher.encrypt(b"session_end"))
                break

if __name__ == "__main__":
    main()
