# Death Note

#### Category : Death Note
#### Points : 454 (43 solves)
#### Author : Mr.Grep

## Challenge
CTF Box based on Death Note
Note : submit the root flag

[chall link](https://tryhackme.com/jr/bsidesnoida2021ctfn6)

## Solution
#### Nmap Scan
Scanning for ports, we see that there are only 2 ports open : 22 and 80.

#### Directory scan
Scanning for directories with the given [wordlst](https://github.com/p1xxxel)

```bash
index.html              [Status: 200, Size: 4173, Words: 1633, Lines: 104]
s3cr3t                  [Status: 200, Size: 63, Words: 12, Lines: 2]
robots.txt              [Status: 200, Size: 17, Words: 3, Lines: 2]
ryuk.apples             [Status: 200, Size: 1766, Words: 9, Lines: 31]
robots.txt              [Status: 200, Size: 17, Words: 3, Lines: 2]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10]
:: Progress: [4614/4614] :: Job [1/1] :: 148 req/sec :: Duration: [0:00:31] :: Errors: 0 ::
```

At `ryuk.apples`, there is a ssh private key but it has a passphrase.

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Death%20Note/ryuk_ssh_passphrase.png">

#### Cracking ssh key
We can use `ssh2john` and then crack it with john using the given wordlist.
<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Death%20Note/cracking_ssh_key.png">

Now we can use this to login as `ryuk`

#### Cracking shadow
We see in ryuk's home directory there is shadow and passwd. 
<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Death%20Note/ryuk_shadow.png">

Using them, we get the password of `light`
<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Death%20Note/cracking_shadow.png">

#### Getting flag
Doing a `sudo -l`, we can run `cat` as root so we can just cat the flag at `/root/root.txt`

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Death%20Note/getting_flag.png">

So the flag is `BSNoida{Pr1vEsc_w4a_E4sy_P3a5y}`