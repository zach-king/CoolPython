from Crypto import Random
from Crypto.Cipher import AES
import tkinter
import tkinter.filedialog
import tkinter.messagebox

key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
key = "D21A90B04A21AD52ED19287023AD9013"

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def encrypt(message, key, key_size=256):
	message = pad(message)
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return iv + cipher.encrypt(message)


def decrypt(ciphertext, key):
	iv = ciphertext[:AES.block_size]
	cipher = AES.new(key, AES.MODE_CBC, iv)
	plaintext = cipher.decrypt(ciphertext[AES.block_size:])
	return plaintext.rstrip(b"\0")


filename = None

def encrypt_file(filename, key):
	with open(filename, 'rb') as f:
		plaintext = f.read()
	enc = encrypt(plaintext, key)
	with open(filename + ".enc", 'wb') as f:
		f.write(enc)


def decrypt_file(filename, key):
	with open(filename, 'rb') as f:
		ciphertext = f.read()
	dec = decrypt(ciphertext, key)
	with open(filename[:-4], 'wb') as f:
		f.write(dec)


def load_file():
	global key, filename
	text_file = tkFileDialog.askopenfile(filetypes=[('Text Files', 'txt')])
	if text_file.name != None:
		filename = text_file.name


def encrypt_the_file():
	global filename, key
	if filename != None:
		encrypt_file(filename, key)
	else:
		messagebox.showerror(title="Error:", message="There was no file loaded to encrypt")


def decrypt_the_file():
	global filename, key
	if filename != None:
		fname = filename + ".enc"
		decrypt_file(fname, key)
	else:
		messagebox.showerror(title="Error:", message="There was no file loaded to decrypt")






root = tkinter.Tk()
root.title("Cryptofile")
root.minsize(width=200, height=200)
root.maxsize(width=200, height=200)


loadButton = tkinter.Button(root, text="Load Text File", command=load_file)
encryptButton = tkinter.Button(root, text="Encrypt File", command=encrypt_the_file)
decryptButton = tkinter.Button(root, text="Decrypt File", command=decrypt_the_file)

loadButton.pack()
encryptButton.pack()
decryptButton.pack()

root.mainloop()
