# Create data folder and path to folder
# Ask user to enter credentials

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)


key = Fernet.gnerete('This is my secret key')

token = f.encrypt(b'my deep dark secret')
print(token)
f.decrypt(token)
