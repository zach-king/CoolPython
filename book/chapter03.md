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
encryption (without the nitty gritty details, which we'll leave for cryptographers).  
Then we'll use a third-party package for Python, known as *PyCrypto*, to write
a very basic encryption/decryption program to use from the command-line.

---

## History:

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

Nowadays, there are two types of encryption: symmetric and asymmetric. 

---

## Wrap Up:

[Prev: Chapter 2 - Sending Email](./chapter02.md) | [Next: Chapter 4 - Web Scraping](./chapter04.md)
