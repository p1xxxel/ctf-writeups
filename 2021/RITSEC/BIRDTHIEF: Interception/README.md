# BIRDTHIEF: Interception

#### Category : Forensics
#### Points : 200(46 solves)
#### Author : f1rhaz4rd

## Challenge

Read the slide deck for more information

Flag format RITSEC{}

F1rhaz4rd

Attachments :

+ BIRDTHIEF.pdf
+ interception.pcapng

## Solution

Open the capture in wireshark and then right click on a TCP protocol capture->Follow->TCP Stream.

Going through the stream one by one, in stream no. 30 we can see someone tries to log into the drone with username `pilot` and a base32 encoded password, which after decrypting becomes `ritsec`.

If we see below that, we can see that the user executes a command

`cat droneinfo.log`

which outputs another base32 string.

Decoding this string, we get the flag:

`RITSEC{Dr0n3_ar3_rea11y_c00l}`
