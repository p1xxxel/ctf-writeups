# Decrypting the payload

#### Category : mission, malware, forensics
#### Points : 100 (56 solves)

## Challenge
We need to know how the attacker gained access to our network.

The team discovered that some of our employees where targeted by a phishing attempt and got this excel file from their emails.

Can you check if this was used to gain a foothold in our network?

Flag format: flag{string}

Attachment : Account_report.xlsm

## Solution
I use olevba on the given xlsm file.

```bash
olevba --reveal --decode Account_report.xlsm
```

Doing this, we get the source code of the macros in the file but it looks like the variables are base64 encoded.
![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Decrypting%20the%20payload/b64_encoded_malware.png)

And then they are executed together.
![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Decrypting%20the%20payload/malware_execution.png)

So I just save only the base64 encoded data into a file(remove the variable names,'=' and 'b') as enc_malware.txt and put the file in cyberchef.

Doing this, we can see the payload used in the malware. I saved this in a file and remove the '.' characters as b64_dec_malware.txt.
![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Decrypting%20the%20payload/cyberchef_b64_dec.png)

Looking at the decoded data, we can spot the flag which is written in reverse.
![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Decrypting%20the%20payload/finding_flag.png)

So the flag becomes `flag{m4cr0_3n4bl3d_d0cs_4r3_d4ng3r0us}`