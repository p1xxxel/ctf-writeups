# Xoro

#### Category : Crypto
#### Points : 380 (89 solves)
#### Author : rey

## Challenge


"You need to accept the fact that you’re not the best and have all the will to strive to be better than anyone you face." – Roronoa Zoro

Connection : `nc 104.199.9.13 1338`

Attachment : xoro.py

## Solution

From the python file we see that it takes some hex input, converts it into bytes, concatenates with the flag bytes and then XORs it with a randomly generated and padded key originally of length 32.

```python
def pad(text, size):
    return text*(size//len(text)) + text[:size%len(text)]
```

As the key is of 32 characters and then it gets padded by the above function, if we input our own 32 characters, we can then XOR the result we get with the characters we sent, to get the key.

```bash
# nc 104.199.9.13 1338                                                                           ─╯

===== WELCOME TO OUR ENCRYPTION SERVICE =====

[plaintext (hex)]>  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[ciphertext (hex)]> 03dbb4aa7bafbdf8c2ba096da1a4868011f49fbb54dd97778749af3266063e2feb22506fb8617629007fd498686f4275c231404e9c0558bc46bc51d089f3cccafb2e2121ee246a
See ya ;)
```

I input 64 A's (2 hex characters = 1 byte) and get the above as cipher text.

I then XOR the payload(bytes from 64 A's) and the first 32 bytes from cipher text, to get the key.

```python
>>> from pwn import xor
>>> cipher = '03dbb4aa7bafbdf8c2ba096da1a4868011f49fbb54dd97778749af3266063e2feb22506fb8617629007fd498686f4275c231404e9c0558bc46bc51d089f3cccafb2e2121ee246a'
>>> key = xor(bytes.fromhex(cipher)[0:32],bytes.fromhex("A"*64))
>>> key
b'\xa9q\x1e\x00\xd1\x05\x17Rh\x10\xa3\xc7\x0b\x0e,*\xbb^5\x11\xfew=\xdd-\xe3\x05\x98\xcc\xac\x94\x85'
```

Now, we can just xor the original cipher text and the key to get the flag.

```python
>>> xor(bytes.fromhex(cipher),key)[32:]
b'BSNoida{how_can_you_break_THE_XOR_?!?!}'
```

So the flag is `BSNoida{how_can_you_break_THE_XOR_?!?!}`

Note : If you use the XOR function from the script, you will first need to pad the key to be of the same lenght as cipher.