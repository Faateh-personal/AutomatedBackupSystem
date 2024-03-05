from cryptography.fernet import Fernet


def encrypt_file(input_filename, output_filename, key):
    """Encrypts a file using Fernet symmetric encryption."""
    cipher = Fernet(key)
    with open(input_filename, 'rb') as file:
        encrypted_data = cipher.encrypt(file.read())
    with open(output_filename, 'wb') as file:
        file.write(encrypted_data)
