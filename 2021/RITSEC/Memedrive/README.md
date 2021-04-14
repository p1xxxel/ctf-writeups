# Memedrive

#### Category : REV/BIN
#### Points : 275 (31 solves)
#### Author : degenerat3

## Challenge

The best Android app for viewing memes!

-degenerat3

Attachment : memedrive.apk

## Solution 

I tried opening the apk using android device/emulator which gave me a screen asking for Username and Password.

Decoding the given apk using apktools :

```
apktool d memedrive.apk
```
We get a folder "memedrive" containing all the resources of the original apk.

From the name we know it contains some memes.

These are located in `memedrive/res/drawable`.

These memes have file name starting with db.

`ls -l db*`

We see there are 10 images.

There are 2 memes that I thought were relevant to the challenge. One of them had a Flag picture with the text RITSEC and a XOR symbol in it.

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RITSEC/Memedrive/db7.png" width="50%" height="50%">

The other one saying about encryption with Base64 and XOR.

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RITSEC/Memedrive/db8.png" width="50%" height="50%">

After that I decompiled the apk using `jadx-gui`.

Going down to `com.ritsecctf.memedrive`, we see there are various classes.

Viewing the code of the class `InitStuff`, we see that the app is getting a text file from github with the name `flags.txt`. 

> https://raw.githubusercontent.com/yung-g4ngst3r360noscope/gimmeThatData/main/flags.txt

If we download the txt file, we get 4000 lines of what looks like base64 encoded flags. Remember the meme about Base64+XOR? That is what will work here. But this is not enough. We need to find the key for XOR to get the flag.

If we view the code of the Showimg[1..10] functions, we see that the app is writing something to a text file called `key.log`.

I wrote a quick python script :

```python
import base64
from pwn import xor

flags = open("flags.txt", 'r')
lines = flags.readlines()
key = '7NFSK27C'
key = bytearray.fromhex(key.encode('ASCII').hex())
for line in lines:
    line_bytes = line.encode('ascii')
    base64_bytes = base64.b64decode(line_bytes)
    letmein = xor(base64_bytes, key)
    message = letmein.decode('ascii')
    if('RS{' in message):
        print(message)
```

I tried the keys one by one and the key that seemed to work was from the class `Showimg7` containing the key `7NFSK27C`.

Running the script, we get the flag :

`RS{4Ndr01d_rEvur5!NG_SuX_1ma0}`
