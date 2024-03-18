# Secure Client-Server Communication System

## Overview

This project demonstrates a secure client-server network facilitating data communications, resource sharing, and distributed systems. Utilizing Python, it establishes a robust client/server network that supports secure data exchange using symmetric encryption. The project caters to varied serialization formats and is designed with an emphasis on modularity and extensibility.

## Key Features

- **Secure Communication**: Implements symmetric encryption using the Fernet module for data security during transmission.
- **Serialization Formats**: Supports multiple data serialization formats including JSON, Binary (Pickle), and XML, catering to diverse client needs.
- **Modular Architecture**: Designed for scalability and ease of modification, allowing for future enhancements without major overhauls.
- **Unit Testing**: Includes comprehensive unit tests for validation of functionality and to ensure reliability and stability.

## Prerequisites

- Python 3.6 or later
- Pip (Python package installer)

## Installation Guide

1. Clone the repository:

---------------------------------------------------
  git clone https://github.com/MrSiNun/mid-module-sinanbilir.git
---------------------------------------------------

2. Navigate to the project directory:

---------------------------------------------------
cd path/to/project
---------------------------------------------------

3. Install the required Python packages:

---------------------------------------------------
pip install -r requirements.txt
---------------------------------------------------

## Usage
This project comprises encryption, server, and client components that communicate over a network. Follow these steps to set up the communication system:

### Encryption Key Generation
Generate an encryption key accessible to both client and server before initiating them:

---------------------------------------------------
python encryption_final.py
---------------------------------------------------

This generates a new encryption key, saved as `encryption.key`, which is used for encrypting and decrypting messages.

### Server Connection
With the key generated, start the server:

---------------------------------------------------
python server_final.py
---------------------------------------------------

### Client Data Collection
Once the server is running and ready to receive client data, start the client:

---------------------------------------------------
python client_final.py
---------------------------------------------------

## Workflow

The communication workflow involves the following steps:

1. **Encryption Key Generation**: Initially, a secure encryption key is generated and stored in a file accessible by both the client and server.
2. **Client and Server Key Loading**: Both the client and the server load the shared encryption key to encrypt and decrypt the transmitted data.
3. **Client Data Collection and Transmission**: The client gathers data from the user, serializes and encrypts it, and then sends it over to the server.
4. **Server Data Reception and Processing**: The server receives the encrypted data, decrypts, deserializes it, and processes it according to the application's logic.
5. **Session Management**: The system is capable of maintaining a continuous data exchange or terminating the session upon completion of the communication.

## Components

### Client

- Collects user data.
- Handles serialization format selection (JSON, binary, or XML).
- Encrypts and sends data to the server.

### Server

- Decrypts received data.
- Handles data deserialization.
- Manages data storage and processing.

### Encryption

- Generates and saves an encryption key.
- Enables symmetric encryption for data security.


## Unit Testing
Run unit tests for the server, client, and encryption modules to ensure reliability:

---------------------------------------------------
python -m unittest server_final_unittest.py
python -m unittest client_final_unittest.py
python -m unittest encryption__final_unittest.py
---------------------------------------------------

## Contributors
We extend our gratitude to the dedicated team members who have contributed to this project:

- Ricardo Migliorini
- Sinan Bilir
- Taras Lalchan
- Tsz Yeung Cheng

For a full list of contributors and their contributions, visit our [GitHub contributors page](https://github.com/MrSiNun/mid-module-sinanbilir.git/contributors).


## License
Specify your project's license here, ensuring it's suitable for open-source collaboration.# csck541-groupC-groupProject
