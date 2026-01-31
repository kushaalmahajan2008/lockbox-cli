import os # used to check if key file already exist or not
from cryptography.fernet import Fernet # used to encrypt or decrypt files

KEY_FILE="secret.key"

def generate_key():
    key=Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_data(data:bytes) -> bytes:
    key=load_key()
    fernet=Fernet(key)
    return fernet.encrypt(data)

def decrypt_data (encrypted_data: bytes) -> bytes:
    key=load_key()
    fernet=Fernet(key)
    return fernet.decrypt(encrypted_data)






