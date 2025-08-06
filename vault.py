import os
from encryption import load_key, load_encrypted_json, save_encrypted_json

def add_password():
    os.system("clear")
    key = load_key()
    data = load_encrypted_json(key)

    alias = input("\nAlias: ")
    username = input("Username: ")
    password = input("Password: ")

    data["accounts"].append({"alias": alias, "username": username, "password": password})
    save_encrypted_json(data, key)

    os.system("clear")
    print("✅ Password added successfully!")
    input("\n👉 Press any key to continue...")

def show_passwords():
    os.system("clear")
    key = load_key()
    data = load_encrypted_json(key)

    for account in data["accounts"]:
        print(f"\nAlias: {account['alias']}\nUsername: {account['username']}\nPassword: {account['password']}")

    input("\n👉 Press any key to continue...")

def modify_password():
    key = load_key()
    data = load_encrypted_json(key)

    while True:
        os.system("clear")
        alias = input("\nAlias to modify: ")

        for account in data["accounts"]:
            if account["alias"] == alias:
                account["password"] = input("New password: ")
                save_encrypted_json(data, key)

                os.system("clear")
                print("✅ Password updated!")
                input("\n👉 Press any key to continue...")

                return
        print("\n❌ Alias not found. Try again.")
        input("\n👉 Press any key to continue...")

def delete_password():
    key = load_key()
    data = load_encrypted_json(key)

    while True:
        os.system("clear")
        alias = input("\nAlias to delete: ")
        before = len(data["accounts"])
        data["accounts"] = [a for a in data["accounts"] if a["alias"] != alias]

        if len(data["accounts"]) < before:
            save_encrypted_json(data, key)
            os.system("clear")
            print("✅ Password deleted!")
            input("\n👉 Press any key to continue...")
            
            return
        else:
            print("\n❌ Alias not found. Try again.")
            input("\n👉 Press any key to continue...")
