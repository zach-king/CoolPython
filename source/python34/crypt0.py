from Crypto.Cipher import AES

# Encryption
encryption_suite = AES.new('key of length 16', AES.MODE_CBC, 'iv of length 16.')
ciphertext = encryption_suite.encrypt("Super secret message. top secret")

# Decryption
decryption_suite = AES.new('key of length 16', AES.MODE_CBC, 'iv of length 16.')
plaintext = decryption_suite.decrypt(ciphertext)

print('Original: Super secret message. top secret')
print('Ciphertext: %s' % ciphertext)
print('Decrypted: %s' % plaintext)
