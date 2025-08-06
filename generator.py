import os
import re
import string
import random

def password_generator():
    while True:
        s1 = list(string.ascii_lowercase)
        s2 = list(string.ascii_uppercase)
        s3 = list(string.digits)
        s4 = list(string.punctuation)

        os.system("clear")
        length = input("How many characters do you want in your password? ")

        try:
            length_int = int(length)
        except:
            print("\n❗ Please enter a number.")

            continue

        if length_int < 8:
            print("\n❗ Your password must have at least 8 characters.")
            input("\n👉 Press any key to continue...")

            continue

        random.shuffle(s1)
        random.shuffle(s2)
        random.shuffle(s3)
        random.shuffle(s4)

        part1 = round(length_int * 0.3)
        part2 = round(length_int * 0.2)

        result = []

        for i in range(part1):
            result.append(s1[i])
            result.append(s2[i])
        for i in range(part2):
            result.append(s3[i])
            result.append(s4[i])

        random.shuffle(result)
        password = "".join(result)

        if re.search(r"[A-Z]", password) and re.search(r"[!@#$%^&*()_+=\\-]", password):
            print(f"\n👀 Your new password: {password}")
            input("\n👉 Press any key to continue...")
            
            break
