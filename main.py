import os
from encryption import generate_key
from authentification import login
from vault import add_password, show_passwords, modify_password, delete_password
from generator import password_generator

def main_page():
    while True:
        os.system("clear")
        print(
            "====== Password Vault ======\n"
            "\n[1] Add a password ➕"
            "\n[2] Show passwords 📋"
            "\n[3] Modify a password ✏️"
            "\n[4] Delete a password ❌"
            "\n[5] Generate a password 🎲"
            "\n[6] Exit 🚪\n"
        )
        option = input("Choose an option: ")

        match option:
            case "1": add_password()
            case "2": show_passwords()
            case "3": modify_password()
            case "4": delete_password()
            case "5": password_generator()
            case "6":
                os.system("clear")
                print("\n👋 Have a nice day!\n")
                
                break
            case _: 
                os.system("clear")
                print("\n❗ Invalid option.")
                input("\n👉 Press any key to continue...")

def main():
    generate_key()
    login()
    main_page()

if __name__ == "__main__":
    main()
