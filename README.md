# crypto-ransomware
A simple malware built using Python to demonstrate how crypto-ransomware works. 

Ransomware is a type of malware from cryptovirology that threatens to publish the victim's personal data or permanently block access to it unless a ransom is paid. This has become a widespread threat in recent years.

## Dependencies
To run this program, you must have the following dependency installed:

```
pip install cryptography
```

## Usage
Run the `encrypt.py` file to encrypt all files in a given directory. It then outputs a ransom message and the number of files encrypted.

Run the `decrypt.py` file to decrypt all the files. This requires a secret phrase or key which is provided by the attacker on successful payment of the ransom. In this case, the secret key is `verysecurepassword`.

Please note that this program is for educational purposes only and should not be used to harm others.