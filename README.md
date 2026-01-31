🔐 LockBox CLI – Encrypted Password Manager
A terminal-based encrypted password manager built in Python.  Stores passwords securely in a local encrypted vault and supports password generation, search, and service listing.
It allows users to save, search, generate, and manage passwords without relying on any cloud service.

The project focuses on security fundamentals, clean logic, and modular design, making it a strong beginner-to-intermediate level project.


🚀 Features

🔒 Encrypted local vault
All passwords are stored in an encrypted file (vault.enc)
Data is unreadable without the encryption key
➕ Add new passwords
Save service name, username/email, password, and optional notes
🔎 Search saved passwords
Quickly retrieve credentials for a specific service
📋 List all services
View all stored service names in the vault
🔑 Password generator
Generate strong passwords with:
custom length
uppercase letters
lowercase letters
numbers
symbols
🖥️ CLI-based interface
Simple, fast, and distraction-free terminal experience



🛠️ Tech Stack
Language: Python 3
Encryption: cryptography (Fernet – symmetric encryption)
Standard Libraries Used:
json
os
secrets
string
No databases. No cloud. Everything runs on-device.



⚙️ Installation & Setup

1️⃣ Clone or download the project
git clone <repo-url>
cd lockbox_cli

2️⃣ Install required dependency
pip install cryptography

3️⃣ Run the application
python main.py



📌 Future Improvements (Optional)
Master password–based encryption
Masked password input
Clipboard copy support
Streamlit GUI version
