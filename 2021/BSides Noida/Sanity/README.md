# Sanity

#### Category : Reverse
#### Points : 437 (56 solves)
#### Author : 1gn1te

## Challenge
```bash
strings Sanity.exe | grep BS | cut -d'{' -f2 | cut -d'}' -f1 | while read l;do echo $l | base64 -d ;done
```

[chall link](https://storage.googleapis.com/noida_ctf/Reverse/Sanity.zip)

## Solution
Using the command given in the challenge we get lyrics of Rickroll.

Opening the exe in ghidra, we see that it XORs each character and then compares it.

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Sanity/ghidra_decompilation.png">

Opening the binary in Ollydbg and setting the breakpoint at the `CMP` instruction using `F2`.

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Sanity/ollydbg_breakpoint.png">

The flag length is 33 as this was the length of the string getting XORed with input(from ghidra).

We send 33 A's and then look at the CMP instruction.

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Sanity/CMP_instruction.png">

So A gets converted into H and then is compared to K. So we can just XOR A with H to get the key and then XOR the key with K to get the flag.

So I note down the encrypted key and the encrypted string and make the following solve script.

```python
from pwn import xor
payload = 'A'*33
cipher = 'HeHeBoiiHeHeBoiiHeHeBoiiHeHeBoiiH'
enc_key = 'KwGKjJISL^s^yTRRs^s^yTRRs^s{EBIOt'
flag = ''
for i in range(0,33):
    flag = flag + xor(xor(enc_key[i],payload[i]),cipher[i]).decode('ascii')
print(flag)
```

Using this script, we get the flag `BSNoida{Ezzzzzzzzzzzzzzzzzz_Flag}`