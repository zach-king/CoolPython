from Crypto import Random
from Crypto.Cipher import AES
import hashlib

def get_hash(msg):
    # Create hash, using msg converted to bytes
    return hashlib.md5(bytes(msg, 'utf-8')).hexdigest()

def pad(s):
    s = bytes(s, 'utf-8')
    s = s + b'\0' * (AES.block_size - len(s) % AES.block_size)
    return s.decode('utf-8')

def encrypt(message, key):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)


def decrypt(ciphertext, key):
	iv = ciphertext[:AES.block_size]
	cipher = AES.new(key, AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(ciphertext[AES.block_size:])
	return plaintext.rstrip(b'\0').decode()

if __name__ == '__main__':
    plaintext = input('Enter message to encrypt: ')
    key = input('Enter key: ')
