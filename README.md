# 🔐 Password Vault – Secure CLI App in Python

A **minimalist and secure command-line password manager** built with Python. This project simulates a mobile password management app but runs entirely in the terminal — combining simplicity, encryption, and good design practices.

---

## 🧠 Features

- ✅ **Master password login** (Argon2 hashed)
- 🔐 **Encrypted JSON storage** using **Fernet symmetric encryption**
- 📁 Password vault with full CRUD:
  - Add / Edit / Delete / View saved credentials
- 🎲 Built-in **strong password generator**
- 🧼 Clean, user-friendly CLI experience
- 🌱 Modular codebase split across logical files

---

## 🧱 Project Structure

```
📁 password-vault/
│
├── encryption.py        # Fernet key generation, encryption & decryption logic
├── authentication.py    # Master password setup + login (hashed with Argon2)
├── vault.py             # Password vault CRUD operations (add, show, edit, delete)
├── generator.py         # Secure password generator (mixed characters)
└── main.py              # Entry point: brings all components together
```

---

## 🛡️ Security Highlights

- **Argon2** for hashing the master password — an industry-standard password hashing algorithm designed to resist brute-force attacks.
- **Fernet** symmetric encryption for securing the `.json` file where all credentials are stored.
- **Hidden encryption key** stored in `.secret.key`, ignored from version control and hidden from plain view.
- No sensitive data exposed in plaintext even after decrypting the vault — master password is always stored hashed.

---

## 🧠 Motivation

This project was built to better understand:

- Real-world password hashing
- Encryption principles
- Modular CLI app architecture in Python

It's also a foundation for a future GUI version or even mobile integration.

---

## 👤 Author

Andrei-Mihnea Dumitrașcu

Student at University POLITEHNICA of Bucharest – Faculty of Automatic Control and Computer Science
