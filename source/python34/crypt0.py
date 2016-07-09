from Crypto.Cipher import AES

# Subject 1 encrypting a message
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = 'The answer is no'
ciphertext = obj.encrypt(message)
print(ciphertext)

# Subject 2 decrypting the ciphertext
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
decrypted = obj2.decrypt(ciphertext)
print(decrypted)
