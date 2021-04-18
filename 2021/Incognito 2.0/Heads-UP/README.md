# Heads-UP

#### Category : Medium
#### Points : 148 (18 solves)

## Challenge

What does this show?

Attachment : headup.txt

#### Hint

It is a stegano challenge

## Solution

Opening the txt file, we see that we are given some coordinates.

Plotting the coordinates using [dcode.fr](https://www.dcode.fr/coordinates-geolocalization) we get :

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/Incognito%202.0/Heads-UP/heads-up.png">

As the locations were very close by and from the name of the challenge, I thought that it might be a constellation. As there are 19 points, I searched for constellation with 19 stars which was `orion`.

The hint says it is a stegano challenge. Searching for steganography in txt files, we get the first link describing about whitespace steganography using a tool `stegsnow`.

Install the tool using :

```
sudo apt install stegsnow
```

We can see from the man page of stegsnow about how to extract the secret message :

>stegsnow -C -p "hello world" outfile

Using `orion` as our key and we run the following command :

```
stegsnow -C -p "orion" headup.txt
```

From this, we get the flag:

`ICTF{Fr0m_Out3r_W0RLD}`
