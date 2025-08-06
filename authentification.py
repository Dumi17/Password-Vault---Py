import os
import re
from getpass import getpass
from argon2 import PasswordHasher
from encryption import load_key, save_encrypted_json, load_encrypted_json

def login():
    key = load_key()
    path = "config.json"

    if os.path.exists(path):
        data = load_encrypted_json(key)
        password1 = data["master_password"]

        while True:
            os.system("clear")
            print("\n👋 Welcome back to Password Vault!")
            password2 = getpass("\nType your password: ")
            ph = PasswordHasher()

            try:
                if ph.verify(password1, password2):
                    os.system("clear")
                    print("\n✅ Logged in successfully!")
                    input("\n👉 Press any key to continue...")

                    break
            except:
                os.system("clear")
                print("\n❌ Incorrect password. Try again!")
                input("\n👉 Press any key to continue...")

    else:
        while True:
            while True:
                os.system("clear")
                print("\n👋 Welcome to Password Vault!")
                new_password1 = getpass("\n✏️ Create a password: ")

                if (
                    len(new_password1) >= 8
                    and re.search(r"[A-Z]", new_password1)
                    and re.search(r"[!@#$%^&*()_+=\\-]", new_password1)
                ):
                    break
                else:
                    os.system("clear")
                    print("\n❗ Password must have at least 8 characters, one uppercase, and one special character.")
                    input("\n👉 Press any key to continue...")

            new_password2 = getpass("Type it again: ")

            if new_password1 == new_password2:
                ph = PasswordHasher()
                data = {"master_password": ph.hash(new_password1), "accounts": []}
                save_encrypted_json(data, key)
                
                os.system("clear")
                print("\n✅ Account created successfully!")
                input("\n👉 Press any key to continue...")

                break
            else:
                os.system("clear")
                print("\n❌ Passwords do not match. Try again!")
                input("\n👉 Press any key to continue...")
