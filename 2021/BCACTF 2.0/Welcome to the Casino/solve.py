#!/usr/bin/python2
from pwn import *
host = "misc.bcactf.com"
port = 49156
while True:
    try:
        s = remote(host, port)
    except:
        continue
    print(s.recvuntil("Let's see"))
    print(s.recv())
    print(s.recv())
    key = (s.recv().split('"')[1])
    s.sendline(key)
    try:
        print(s.recvuntil("bcactf"))
        print(s.recv())
        break
    except:
        continue

