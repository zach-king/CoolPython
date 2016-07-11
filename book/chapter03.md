# Chapter 3: Cryptography

[Prev: Chapter 2 - Sending Email](./chapter02.md) \| [Next: Chapter 4 - Web Scraping](./chapter04.md)

## Summary:

These days everyone carries gigabytes--even terabytes--of data on them at all times. Thus, we
face a very important task--keeping that data locked down tight and out of the wrong hands! That's
where the fun of cryptography comes in.

You may have seen some examples of encryption before, and perhaps thought it
would be just as hard to write an encryption program as it is to crack the
cipher behind it. But fear not, for nothing is so challenging with Python--seriously,
this chapter will make you look like a genius \(but of course you are one...\).

So what we'll go through in this chapter is first some basic study of modern
encryption \(without _all_ the nitty gritty details, which we'll leave for cryptographers\).  
Then we'll use a third-party package for Python, known as _PyCrypto_, to write
a very basic encryption\/decryption program to use from the command-line.

Please bare in mind that cryptography isn't a menial topic and so before we can start writing our glorious cyber security code, we must first examine the subject itself. That doesn't mean I'm going to describe verbatim the bit-level in's and out's of AES \(Advanced Encryption Standard\) or similar discussions \(though I'm sure you'd be totally interested in all that\).

---

## History of Cryptography:

Before moving into the meat of this chapter, I'd like to give a brief history
lecture regarding the origins of cryptography. If you find this boring, or already
know it all, feel free to skip to the [good stuff](#content).

The true origins of cryptography date way back all the way to the Egyptians. They
of course used hieroglyphs to communicate, and only the scribes knew these glyphs.
Later, a more well-known instance of encryption was used by Julius Caesar for private
communication; this encryption involved shifting the letters in the message by
a certain number--a _key_--and is known as the _Caesar Cipher_.

It wasn't until World War II that cryptography became extremely mathematical. During
the war it was used by armies to communicate without the worry of the enemy obtaining
the information. A very prominent figure of this time is Alan Turing, who cracked
the infamous Enigma Cipher used by the Germans. Arguably, one might say this is what
led to The Allies winning the war.

## Content

First, let's cover some basic concepts of cryptography. Cryptography is defined as
"the art of writing or solving codes." Quite a generic definition, but that just shows
how broad the topic truly is. In most instances of cryptography there are two
primary components: _plaintext_ and _ciphertext_. The plaintext is the message,
or data, in which you wish to keep secret, yet it is simply...plain; the message is
just sitting there waiting for people to read. Ciphertext is the _encrypted_
version of the plaintext; this is how data is kept secure. So how does one's data
go from plaintext to ciphertext?

Well, there are a variety of cryptographic methods for this task. Some involve
shuffling the characters, exchanging characters, and more realistically, manipulating
the data on a bit level. All of these methods make use of a _key_ however. This is
how the message is _decrypted_ back to its original, readable format.

Nowadays, there are two types of encryption: symmetric and asymmetric. Symmetric algorithms, also known as _secret key_ algorithms, use the same key for both encrypting and decrypting data. However, asymmetric  algorithms, also known as _public key_ algorithms, use a different key for encrypting and decrypting data. Regardless of the algorithm used though, there is always one or more keys, and this presents some challenges in itself. It is easily arguable to say that the security in cryptography lies not so much in the algorithm of encryption\/decryption, but rather the careful handling of key\(s\).

So how _should_ we handle these keys? First, we should solve the task of management, or storage, of key\(s\). Keys should be kept very secure, yet still be available to those that need them. This brings us to the second task--distributing the keys. We must be able to securely communicate the key\(s\) to those that need them. In order to solve these problems, let us examine symmetric and asymmetric algorithm properties more closely.

### Asymmetric Algorithms

Again, asymmetric algorithms use a different key for encryption and decryption of data. When a message is sent, the sender uses _their public key_. Then, the receiver uses _their private key_. Don't let the keywords public\/private confuse you; here it is better understood as encryption key and decryption key, respectively.

The primary benefit of asymmetric algorithms is that it does not need to communicate, or distribute, keys at all. The number of keys is effectively twice the number of "subjects" \(i.e. people\), or _2n_, which tells us the complexity analysis of these algorithms is _O\(n\)_.

### Symmetric Algorithms

Symmetric, or _secret key_ algorithms use the same key for both encryption and decryption. Typically, these keys are randomly generated _n_-bit strings, and key sizes are not necessarily related to the security of the encryption.

This algorithm requires that the key be shared between a pair of users; or with several users, each pair of users shares one key. Please note that the keys in asymmetric algorithms and symmetric algorithms are not directly comparable.

### Stream Ciphers

Next, we should take a look at the two types of ciphers, stream and block ciphers. First let's discuss stream ciphers. Stream ciphers take one symbol at a time and convert them into a ciphertext symbol. The Caesar Cipher is an example of a stream cipher because each character is translated to another.

The advantages of stream ciphers are the speed and reliability. These ciphers are linear in time, or _O\(n\)_, and if an error occurs, it only occurs for that symbol. However, stream ciphers convey all of the information of the plaintext symbol in the ciphertext symbol, which usually makes them less secure.

### Block Ciphers

Block ciphers on the other hand encrypt an entire group, or "block", of plaintext at a time. An example of block cipher is the simple transposition cipher in which the symbols are divided into blocks according to the given key, placed in a grid format with each block being a row, and then outputted by column. Most modern symmetric encryption algorithms use the block cipher.

The advantages of block ciphers are that the information regarding the plaintext is dispersed into multiple ciphertext symbols, and it is nearly impossible to insert symbols without noticing the change in ciphertext. However, block ciphers are typically much slower than stream ciphers and a single erroneous symbol will likely affect the entire block of ciphertext.

### Code Please?

Alright, alright, now we can start writing code. The algorithm I will be using is the symmetric cipher known as AES \(Advanced Encryption Standard\). AES is considered one of the most secure encryption algorithms, and it is used by the U.S. government to protect classified data. AES is a block cipher and takes blocks of 128 bits, or . The key for AES can be either 128, 192, or 256 bits long. Though I'm not going to discuss the details of AES, it does make for an interesting study and I suggest you look into it if you would like to learn more.

The Python library I will use is _PyCrypto_. To install PyCrypto, you can use a package manager such as _pip_ or _easy\_install_. Just open your terminal of choice and use the appropriate command:

```
pip install PyCrypto
```

```
easy_install PyCrypto
```

The PyCrypto package offers a healthy amount of cryptographic tools, as well as a better _Random_ module than Python's built-in _random_. Let's take a look at a very simple example taken from the PyCrypto documentation on the Python Package Index page:

```python
# Example 3-1 (crypt0.py)
from Crypto.Cipher import AES

obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = 'The answer is no'
ciphertext = obj.encrypt(message)
print(ciphertext)
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
decrypted = obj2.decrypt(ciphertext)
print(decrypted)
```

Which, when run, yields the following output:

    \xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1
    The answer is no

Now let's "decipher" the meaning of this code. After importing the appropriate submodule from PyCrypto \(import name is actually _Crypto_\), we first need to create a cipher object. This object, an instance of the _AES_ class in _Crypto.Cipher_, is used to encrypt and decrypt.

The constructor of this class takes a few arguments. The first is the key as a string, and the other two are special. _AES.MODE\_CBC_ tells the cipher object to use the Cipher Block Chaining mode; block ciphers use modes such as these. If you read about CBC, you will see that "\[I\]n CBC, each block of plaintext is XORed with the previous ciphertext block before being encrypted" \([source](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_.28CBC.29)\). The last argument is a string, known as the IV. IV stands for initialization vector. The IV should be random, or pseudorandom, and its usage for block ciphers depends on the mode. In our case, using CBC mode, the IV modifies how the first block is encrypted\/decrypted; furthermore, a one-bit change of the IV will result in different results. The following image, obtained from the [wiki page for block ciphers](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_.28CBC.29), depicts the process for encryption using CBC.

![CBC mode encryption](https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/CBC_encryption.svg/601px-CBC_encryption.svg.png)

Next, we store our message as a string, and pass it to the _encrypt\(\)_ method in the cipher object instance. The result of this is a string of bytes, which we store in the _ciphertext_ variable. The code up to this point can be thought of as the "sender" code, and the code afterwards as the "receiver."

On the receiving end, the cipher object must be created first and foremost, in the same manner as the sender. Then, we use the _decrypt\(\)_ method of the cipher object and store the returned plaintext. Easy peasy lemon squeezy, right!

The next step is integrating this with a useful application. So let's write a file encryption program! Before jumping into our favorite text editor \(Atom of course\), we should determine the goal of the application. Basically, I want the application to:

* get a file path from the user, for the plaintext input
* get a file path from the user, for the ciphertext output
* get the key from the user
* use optional command-line arguments 

After laying out these requirements, I wrote the following application:

```python
# Example 3-2 (crypt1.py)
from Crypto import Random
from Crypto.Cipher import AES
import base64, hashlib
import sys


# A helper class for AES encryption/decryption
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
    # Parse and use any command-line arguments
    # sys.argv[0] is the name of the file (crypt1.py) and always present
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

```

While this code might appear a bit daunting, it's really just an extension of the last example. I first wrote a helper class for running the encryption\/decryption, which you can reuse for other projects.

The _AESCipher_ class is initialized with a key, which gets transformed into a SHA-256 digest. The class automatically generates a IV. We want to be able to encrypt data of any size though, not just the block size, since AES is a block cipher; for this reason, we need to _pad_ the data. The _\_pad\(\)_ method fills the remaining space to meet the block size, with a calculated value. Since the padding character is calculated, the inverse method, _\_unpad\(\)_, can strip the necessary amount of padding characters away, based off of just one of them. This padding\/unpadding allows the data to meet the block size requirement regardless of the actual data length. The rest of the class's code is fairly straightforward.

Next, the _main\(\)_ function takes the needed arguments for encrypting or decrypting the contents of a input file and writing the results to a output file. The _if_ clause at the end checks if the script was run, not imported, and if so it uses any command-line arguments given and passes the arguments to _main\(\)_.

You can test this program in a variety of ways, thanks to the acceptance of command-line arguments. Here's one example, which passes all the arguments \(input file, output file, mode, key\):

```
python crypt1.py secret.txt secret.enc 1 shrubbery
```

Which transforms this plaintext \(_secret.txt_\):

```
super secret
text file
```

into this ciphertext \(_secret.enc_\):

```
1n5wILYmZvgmrl0PCCYAAsGBV31Q4ZVhpC16zdAaqu5OP/D3uLY+NXA29qpTTzzN
```

Unfortunately, I won't demonstrate other algorithms here. If you are interested in cryptography and would like to delve further, I would recommend looking into PGP \(Pretty Good Privacy\). PGP is another symmetric algorithm, invented by Phil Zimmerman in 1991; the story around PGP and Zimmerman is very intriguing. To give you an idea of the story around the algorithm, PGP is considered to be unbreakable and the closest you'll get to military-grade encryption...

---

## Wrap Up:

Okay cyber ninjas, now you can wield the power of cryptography in your own projects! Cyber security is a vast and brilliant topic to study, and Python has a lot to offer for exploring it. You should always keep security and privacy in mind when developing applications that handle user data. I will also suggest considering what ethical concerns your project or application might raise and how you should approach them.

Things to remember from this chapter are the two types of cryptography algorithms: symmetric and asymmetric, which translates to using one key or two keys, respectively. Also remember there are two types of ciphers: block and stream ciphers, which accept data in different forms \(chunks or symbol-by-symbol\).

[Prev: Chapter 2 - Sending Email](./chapter02.md) \| [Next: Chapter 4 - Web Scraping](./chapter04.md)

