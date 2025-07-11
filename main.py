import os
import json
import re


def login():
    path = "config.json"

    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
            password1 = data["password"]

            while True:
                password2 = input("\nType your password: ")

                if password1 == password2:
                    print(
                        "\n#######################"
                        "\nLogged in successfully!"
                        "\n#######################\n"
                    )

                    break
                else:
                    print(
                        "\n##############################"
                        "\nIncorrect password! Try again!"
                        "\n##############################\n"
                    )
    else:
        with open(path, "w") as f:
            while True:
                while True:
                    new_password1 = input("\nCreate a password: ")

                    if (
                        len(new_password1) >= 8
                        and bool(re.search(r"[A-Z]", new_password1))
                        and bool(re.search(r"[!@#$%^&*()_+=\-]", new_password1))
                    ):
                        break
                    else:
                        print(
                            "\n#####################################################"
                            "\nPassword should be at least 8 characters long with 1\n" 
                            "minimum upper case and 1 minimum special character"
                            "\n#####################################################\n"
                        )

                new_password2 = input("Type it again: ")

                if new_password1 == new_password2:
                    print(
                        "\n#############################"
                        "\nAccount created successfully!"
                        "\n#############################\n"
                    )

                    data = {"master_password": new_password1}
                    json.dump(data, f)

                    break
                else:
                    print(
                        "\n##################################"
                        "\nPasswords do not match! Try again!"
                        "\n##################################\n"
                    )
    

def add_account():
    alias = input("\nAlias: ")
    username = input("Username: ")
    password = input("Password: ")

    with open("config.json", "r") as f:
        data = json.load(f)

        if "accounts" not in data:
            data["accounts"] = []

        account = {
            "alias": alias,
            "username": username,
            "password": password
        }
        data["accounts"].append(account)
    
    with open("config.json", "w") as f:
        json.dump(data, f)


def delete_account():
    ...


def main_page():
    option = 0  

    while option != 5:
        print(
            "\n##########################"
            "\nWelcome to Password Vault!"
            "\n##########################\n"
            "\n[1] Add an account"
            "\n[2] Modify an account"
            "\n[3] Delete an account"
            "\n[4] Generate a password"
            "\n[5] Exit\n\n"
        )
        option = input("Type your option: ")

        match option:
            case "1":
                add_account()
            case "2":
                ...
            case "3":
                delete_account()
            case "4":
                ...
            case "5":
                option = 5
                print(
                    "\n################"
                    "\nHave a nice day!"
                    "\n################\n"
                )
                break
            case default:
                print("Select a correct number!")

def main():
    login()
    main_page()


if __name__ == "__main__":
    main()
