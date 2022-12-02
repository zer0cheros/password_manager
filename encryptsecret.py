from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
f = Fernet(key)
secret = b"chris1234"
encrypted_secret = f.encrypt(secret)


with open('secret.txt', 'wb') as f:
    f.write(encrypted_secret)



