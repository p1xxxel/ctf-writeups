import base64
from pwn import xor

flags = open("flags.txt", 'r')
lines = flags.readlines()
key = '7NFSK27C'
key = bytearray.fromhex(key.encode('ASCII').hex())
for line in lines:
    line_bytes = line.encode('ascii')
    base64_bytes = base64.b64decode(line_bytes)
    letmein = xor(base64_bytes, key)
    message = letmein.decode('ascii')
    if('RS{' in message):
        print(message)
