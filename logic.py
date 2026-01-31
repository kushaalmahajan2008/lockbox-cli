import os #used to check if vault file exists
import json
from encryption_logics import encrypt_data, decrypt_data
import secrets
import string

vault_file= "vault.enc"


def load_vault(): #takes encrypted data and convert into python dict
    if not os.path.exists(vault_file):
        return {}
    with open (vault_file,"rb") as f:
        encrypted_data=f.read()

    decrypted_data= decrypt_data(encrypted_data)
    return json.loads(decrypted_data.decode())


def save_vault(vault_data:dict): #converts dict to encrypted data and then save in vault
    json_data=json.dumps(vault_data)
    encrypted_data= encrypt_data(json_data.encode())

    with open(vault_file, "wb") as f:
        return f.write(encrypted_data)


def add_new_password():
    vault=load_vault()

    service_name= input("Service name: ").strip().lower()
    if service_name in vault:
        print(f'Password already exists for {service_name}')
        return
    username= input("Username / Email: ").strip()
    password= input("Password: ").strip()
    note = input("Note (optional): ")

    vault[service_name]={
        "username": username,
        "password": password,
        "note" : note
        }
    
    save_vault(vault)
    print("Password saved successfully.")


def password_generator():
        while True:
            try:
                length =int(input("Password length (8-32): "))
            except:
                print("Please enter a number between 8 and 32\n")
                continue
            if length<8 or length>32:
                print("Length must be between 8 and 32\n")
                continue
            
            use_upper= input("Include uppercase letters? (y/n): ").strip().lower()=="y"
            use_lower=input("Include lowercase letters? (y/n): ").strip().lower()=="y"
            use_digits= input("Include digits letters? (y/n): ").strip().lower()=="y"
            use_symbols= input("Include symbils letters? (y/n): ").strip().lower()=="y"

            characters=""

            if use_upper:
                characters+= string.ascii_uppercase
            if use_lower:
                characters+= string.ascii_lowercase
            if use_digits:
                characters+= string.digits
            if use_symbols:
                characters+= string.punctuation

            if not characters:
                print("You must select at least one character type.\n")
                continue

            password="".join(secrets.choice(characters) for _ in range(length))
            return password
        


def search_password():
    vault=load_vault()
    if not vault:
        print("Print vault is empty")
        return
    service= input("Enter service name to search: ").strip().lower()

    if service not in vault:
        print("No password found for this service.")
        return
    
    entry = vault[service]
    print("\nPassword Found!")
    print(f"Sevice: {service}")
    print(f"Username : {entry['username']}")
    print(f"Password : {entry['password']}")

    if entry.get("note"):
        print(f'Note  : {entry['note']}')


def list_services ():
    vault=load_vault()

    if not vault:
        print("Print vault is empty")
        return  
    print("\nList of services saved in vault is:")
    for key in vault:
        print(key)
        