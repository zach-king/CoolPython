"""
File: cryptopress.py
Author: Zachary King
Description: Cryptopress translates to 'cryptography compression.'
    As the name suggests, this program
    takes an arbitrary number of files as input and
    produces a single stream of ciphertext, which
    is the AES encrypted content. Optionally, you can
    output the ciphertext to a file--an archive. Then you can
    use this program to do the inverse action and
    produce the original file(s) from the archive file.
"""

from Crypto import Random
from Crypto.Cipher import AES
import base64, hashlib
import sys, os
import argparse

class AESCipher(object):
    """
    Encrypt and decrypt data with the AES cipher. Uses SHA-256 digests for keys.
    """

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



def dump_ciphertext(in_file, key):
    """Returns the in_file data, encrypted using the key."""
    cipher = AESCipher(key)
    with open(in_file, 'rb') as f:
        data = f.read()
    return cipher.encrypt((in_file + '::::\n').encode('utf-8') + data)


def dump_multiple(key, files, output_file=None):
    """Dump the ciphertext for each file in files to the output_file."""
    cipher = AESCipher(key)

    full_data = b''
    for arg in files:
        full_data += dump_ciphertext(arg, key) + b'\n'

    if output_file != None:
        with open(output_file, 'wb') as f:
            f.write(full_data)

    return full_data


def restore_files(key, mumbofile):
    """Restore the orgiginal files from the compressed archive."""
    cipher = AESCipher(key)

    with open(mumbofile, 'r') as f:
        lines = f.readlines()

    for ciphertext in lines:
        decrypted = cipher.decrypt(ciphertext)
        fname, data = decrypted.decode('utf-8').split('::::\n')
        with open(fname, 'wb') as f:
            f.write(data.strip('\n').encode('utf-8'))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='One or more files for input to mumbojumbo', nargs='+')
    parser.add_argument('-o', '--output', help='An output file to write ciphertext to')
    parser.add_argument('-r', '--restore', help='Restore original file(s) from the given file')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete original file(s) after writing to an output file')
    parser.add_argument('key', help='The key to be used')
    args = parser.parse_args()

    if args.delete and not args.output:
        print('You cannot delete the original file(s) without outputting ciphertext to output.')
        sys.exit(0)

    if args.restore:
        restore_files(args.key, args.restore)
    else:
        dump_multiple(args.key, args.file, args.output)

    if args.delete:
        for fname in args.file:
            os.remove(fname)
