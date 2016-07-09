from Crypto import Random
from Crypto.Cipher import AES
import base64, hashlib
import sys

class AESCipher(object):
    def __init__(self, key):
        # Store SHA-256 digest of key
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.bs = 32

    def _pad(self, s):
        area_to_pad = self.bs - len(s) % self.bs
        padding = area_to_pad * chr(area_to_pad)
        return s.decode('utf-8') + padding

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, data):
        data = self._pad(data)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(data))

    def decrypt(self, ciphertext):
        ciphertext = base64.b64decode(ciphertext)
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(ciphertext[AES.block_size:]))


def main(in_file, out_file, mode, key):
    # Create the Cipher
    cipher = AESCipher(key)
    data = None
    transformed = None

    # Store the data from input file
    with open(in_file, 'rb') as f:
        data = f.read()

    # Should encrypt or decrypt?
    if mode == 1:
        transformed = cipher.encrypt(data)
    else:
        transformed = cipher.decrypt(data)

    # Output the encrypted/decrypted data to out_file
    with open(out_file, 'wb') as f:
        f.write(transformed)

    msg = ''
    if mode:
        msg += 'Encrypted '
    else:
        msg += 'Decrypted '

    print(msg + 'contents of ' + in_file + ' to ' + out_file)



if __name__ == '__main__':
    if len(sys.argv) == 5:
        main(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4])
    elif len(sys.argv) == 4:
        key = input('Enter a key: ')
        main(sys.argv[1], sys.argv[2], int(sys.argv[3]), key)
    elif len(sys.argv) == 3:
        mode = int(input('Encrypt(1) or Decrypt(0): '))
        key = input('Enter a key: ')
        main(sys.argv[1], sys.argv[2], mode, key)
    elif len(sys.argv) == 2:
        out_file = input('Output filename: ')
        mode = int(input('Encrypt(1) or Decrypt(0): '))
        key = input('Enter a key: ')
        main(sys.argv[1], out_file, mode, key)
    else:
        in_file = input('Input filename: ')
        out_file = input('Output filename: ')
        mode = int(input('Encrypt(1) or Decrypt(0): '))
        key = input('Enter a key: ')
        main(in_file, out_file, mode, key)
