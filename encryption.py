import os
import json
from cryptography.fernet import Fernet

KEY_FILE = ".secret.key"
VAULT_FILE = "config.json"

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_data(data, key):
    f = Fernet(key)

    return f.encrypt(data.encode())

def decrypt_data(data, key):
    f = Fernet(key)

    return f.decrypt(data).decode()

def save_encrypted_json(data, key):
    encrypted = encrypt_data(json.dumps(data), key)

    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)

def load_encrypted_json(key):
    with open(VAULT_FILE, "rb") as f:
        encrypted = f.read()

    decrypted = decrypt_data(encrypted, key)
    
    return json.loads(decrypted)
