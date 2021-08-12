# Welcome to the challenge

#### Category : forensics, images
#### Points : 100 (197 solves)

## Challenge
Welcome to the RCTS Challenge!

Can you find the flag?

Flag format: flag{string}

Attachment : rcts_challenge.jpg

## Solution
Using the `Extract Files` operation in Cyberchef on the given image file, we see that it might contain 6 files including a png file.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Welcome%20to%20the%20challenge/cyberchef_extracted.png)

Clicking this png file, gives us the flag.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Welcome%20to%20the%20challenge/getting_flag.png)

So the flag is `flag{0n3_1m4g3_1s_n0t_3n0ugh}`