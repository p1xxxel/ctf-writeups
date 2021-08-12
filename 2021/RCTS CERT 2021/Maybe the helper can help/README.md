# Maybe the helper can help

#### Category : forensics
#### Points : 100 (98 solves)

## Challenge

You might not see it, but a flag lies within.

Flag Format: flag{string}

Attachment : the-jetsons-family.jpg

## Solution

Using stegseek on this we get the keyphrase is `rosie`

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Maybe%20the%20helper%20can%20help/stegseek_crack.png)

The extracted file contains the flag which has been base64 encoded twice.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Maybe%20the%20helper%20can%20help/getting_flag.png)