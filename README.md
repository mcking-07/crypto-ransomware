# crypto-ransomware
A simple malware built using python to demonstrate how crypto-ransomware works.

Ransomware is a type of malware from cryptovirology that threatens to publish the victim's personal data or permanently block access to it unless a ransom is paid. It has become very popular in recent years.

To install the dependencies
1. cryptography
> pip install cryptography

## Usage
Run the `encrypt.py` file to encrypt all files in a given directory. It then outputs a ransom message and the number of files encrypted.

Run the `decrypt.py` file to decrypt all the files. This requires a secret phrase or key which is provided by the attacker on successful payment of the ransom. In this case it's `verysecurepassword`.