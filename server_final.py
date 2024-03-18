import socket
from cryptography.fernet import Fernet
import json
import pickle
import xml.etree.ElementTree as ET

def load_encryption_key():
    """
    Loads the encryption key from a file named 'encryption.key'.
    """
    with open("encryption.key", "rb") as key_file:
        return key_file.read()

def deserialize_data(encrypted_data, cipher):
    """
    Decrypts and determines the format of the encrypted data,
    attempting to deserialize it accordingly.
    
    Args:
        encrypted_data: The encrypted data received from the client.
        cipher: The Fernet cipher for decryption.

    Returns:
        A tuple (format_detected, deserialized_data) where format_detected
        is the format of data ('json', 'binary', 'xml', 'session_end', or 'unknown')
        and deserialized_data is the deserialized Python object or error message.
    """
    data = cipher.decrypt(encrypted_data)

    # Handle session end signal
    if data == b"session_end":
        return "session_end", None

    # Try to deserialize as binary directly without decoding
    try:
        return "binary", pickle.loads(data)
    except Exception:
        pass  # Proceed to try other formats if binary fails

    # Attempt to decode as UTF-8 for JSON or XML
    try:
        decoded_data = data.decode('utf-8')
    except UnicodeDecodeError:
        return "error", "Data cannot be decoded as UTF-8."

    # Try to deserialize as JSON
    try:
        return "json", json.loads(decoded_data)
    except json.JSONDecodeError:
        pass

    # Try to deserialize as XML
    try:
        root = ET.fromstring(decoded_data)
        return "xml", {child.tag: child.text for child in root}
    except ET.ParseError:
        pass

    return "unknown", "Data format is unknown."

def main():
    """
    Main function to initialize the server, accept connections,
    and process incoming encrypted data from clients.
    """
    encryption_key = load_encryption_key()
    cipher = Fernet(encryption_key)
    
    HOST, PORT = 'localhost', 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")

            while True:
                encrypted_data = conn.recv(4096)
                if not encrypted_data:
                    break  # End loop if no data is received

                format_detected, deserialized_data = deserialize_data(encrypted_data, cipher)
                if format_detected == "session_end":
                    print("Session end signal received. Closing connection.")
                    break

                if deserialized_data:
                    print(f"Data format: {format_detected}")
                    print(f"Received and deserialized data: {deserialized_data}")
                else:
                    print("Failed to deserialize data. Format unknown or data corrupted.")

if __name__ == "__main__":
    main()
