# Chapter 3: Cryptography

[Prev: Chapter 2 - Sending Email](./chapter02.md) | [Next: Chapter 4 - Web Scraping](./chapter04.md)

## Summary:

These days everyone carries gigabytes--even terabytes--of data on them at all times. Thus, we
face a very important task--keeping that data locked down tight and out of the wrong hands! That's
where the fun of cryptography comes in.

You may have seen some examples of encryption before, and perhaps thought it
would be just as hard to write an encryption program as it is to crack the
cipher behind it. But fear not, for nothing is so challenging with Python--seriously,
this chapter will make you look like a genius (but of course you are one...).

So what we'll go through in this chapter is first some basic study of modern
encryption (without *all* the nitty gritty details, which we'll leave for cryptographers).  
Then we'll use a third-party package for Python, known as *PyCrypto*, to write
a very basic encryption/decryption program to use from the command-line.  

Please bare in mind that cryptography isn't a menial topic and so before we can start writing our glorious cyber security code, we must first examine the subject itself. That doesn't mean I'm going to describe verbatim the bit-level in's and out's of AES (Advanced Encryption Standard) or similar discussions (though I'm sure you'd be totally interested in all that). 

---

## History of Cryptography:

Before moving into the meat of this chapter, I'd like to give a brief history
lecture regarding the origins of cryptography. If you find this boring, or already
know it all, feel free to skip to the [good stuff](#content).  

The true origins of cryptography date way back all the way to the Egyptians. They
of course used hieroglyphs to communicate, and only the scribes knew these glyphs.
Later, a more well-known instance of encryption was used by Julius Caesar for private
communication; this encryption involved shifting the letters in the message by
a certain number--a *key*--and is known as the *Caesar Cipher*.

It wasn't until World War II that cryptography became extremely mathematical. During
the war it was used by armies to communicate without the worry of the enemy obtaining
the information. A very prominent figure of this time is Alan Turing, who cracked
the infamous Enigma Cipher used by the Germans. Arguably, one might say this is what
led to The Allies winning the war.

## Content
First, let's cover some basic concepts of cryptography. Cryptography is defined as
"the art of writing or solving codes." Quite a generic definition, but that just shows
how broad the topic truly is. In most instances of cryptography there are two
primary components: *plaintext* and *ciphertext*. The plaintext is the message,
or data, in which you wish to keep secret, yet it is simply...plain; the message is
just sitting there waiting for people to read. Ciphertext is the *encrypted*
version of the plaintext; this is how data is kept secure. So how does one's data
go from plaintext to ciphertext?  

Well, there are a variety of cryptographic methods for this task. Some involve
shuffling the characters, exchanging characters, and more realistically, manipulating
the data on a bit level. All of these methods make use of a *key* however. This is
how the message is *decrypted* back to its original, readable format.

Nowadays, there are two types of encryption: symmetric and asymmetric. Symmetric algorithms, also known as *secret key* algorithms, use the same key for both encrypting and decrypting data. However, asymmetric  algorithms, also known as *public key* algorithms, use a different key for encrypting and decrypting data. Regardless of the algorithm used though, there is always one or more keys, and this presents some challenges in itself. It is easily arguable to say that the security in cryptography lies not so much in the algorithm of encryption/decryption, but rather the careful handling of key(s). 

So how *should* we handle these keys? First, we should solve the task of management, or storage, of key(s). Keys should be kept very secure, yet still be available to those that need them. This brings us to the second task--distributing the keys. We must be able to securely communicate the key(s) to those that need them. In order to solve these problems, let us examine symmetric and asymmetric algorithm properties more closely.

### Asymmetric Algorithms
Again, asymmetric algorithms use a different key for encryption and decryption of data. When a message is sent, the sender uses *their public key*. Then, the receiver uses *their private key*. Don't let the keywords public/private confuse you; here it is better understood as encryption key and decryption key, respectively. 

The primary benefit of asymmetric algorithms is that it does not need to communicate, or distribute, keys at all. The number of keys is effectively twice the number of "subjects" (i.e. people), or *2n*, which tells us the complexity analysis of these algorithms is *O(n)*.

### Symmetric Algorithms
Symmetric, or *secret key* algorithms use the same key for both encryption and decryption. Typically, these keys are randomly generated *n*-bit strings, and key sizes are not necessarily related to the security of the encryption. 

This algorithm requires that the key be shared between a pair of users; or with several users, each pair of users shares one key. Please note that the keys in asymmetric algorithms and symmetric algorithms are not directly comparable.  

### Stream Ciphers
Next, we should take a look at the two types of ciphers, stream and block ciphers. First let's discuss stream ciphers. Stream ciphers take one symbol at a time and convert them into a ciphertext symbol. The Caesar Cipher is an example of a stream cipher because each character is translated to another. 

The advantages of stream ciphers are the speed and reliability. These ciphers are linear in time, or *O(n)*, and if an error occurs, it only occurs for that symbol. However, stream ciphers convey all of the information of the plaintext symbol in the ciphertext symbol, which usually makes them less secure. 

### Block Ciphers
Block ciphers on the other hand encrypt an entire group, or "block", of plaintext at a time. An example of block cipher is the simple transposition cipher in which the symbols are divided into blocks according to the given key, placed in a grid format with each block being a row, and then outputted by column. Most modern symmetric encryption algorithms use the block cipher. 

The advantages of block ciphers are that the information regarding the plaintext is dispersed into multiple ciphertext symbols, and it is nearly impossible to insert symbols without noticing the change in ciphertext. However, block ciphers are typically much slower than stream ciphers and a single erroneous symbol will likely affect the entire block of ciphertext. 

### Code Please?
Alright, alright, now we can start writing code. I will show two different encryption algorithms, one symmetric and one asymmetric. The symmetric encryption algorithm I will be using is AES (Advanced Encryption Standard). AES is considered one of the most secure encryption algorithms, and it is used by the U.S. government to protect classified data. AES is a block cipher and takes blocks of 128 bits. The key for AES can be either 128, 192, or 256 bits long. Though I'm not going to discuss the details of AES, it does make for an interesting study and I suggest so if you would like to learn more. 

The Python package I will use is...(todo)

---

## Wrap Up:

[Prev: Chapter 2 - Sending Email](./chapter02.md) | [Next: Chapter 4 - Web Scraping](./chapter04.md)
