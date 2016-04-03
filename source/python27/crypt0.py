from Crypto import Random
from Crypto.Cipher import AES
import hashlib

def get_hash(msg):
    # Create hash, using msg converted to bytes
    return hashlib.md5(bytes(msg, 'utf-8')).hexdigest()

def pad(s):
    # Pad s with the terminal byte until len(s) is multiple of block_size
    s = bytes(s, 'utf-8')
    s = s + '\x00' * (AES.block_size - len(s) % AES.block_size)
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
    # Text to encrypt
    plaintext = "super secret message. sshhh....."
    print('padded: %s' % pad(plaintext))

    # md5 hash of key string. Use this as the actual key
    key_hash = hashlib.md5(b'my key').hexdigest()

    # Encryption:
    #plaintext = pad(plaintext) # Pad plaintext to right length
    iv = Random.new().read(AES.block_size) # A salt for the cipher
    cipher = AES.new(key_hash, AES.MODE_CBC, iv) # Create AES cipher object
    ciphertext = iv + cipher.encrypt(plaintext) # Encrypt the text
    print('Ciphertext: %s' % ciphertext)

    # Decryption:
    decrypted = cipher.decrypt(ciphertext[AES.block_size:])
    print('Decrypted: %s' % decrypted)
