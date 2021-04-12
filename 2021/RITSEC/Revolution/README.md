# Revolution

#### Category : Web
#### Points : 250 (29 solves)
#### Author : f1rehaz4rd

## Challenge

The robots are taking over. They are posting their propaganda everywhere. Go here to find out more about it.

34.69.61.54:8799

You will need a valuable piece of information from the 'robots' challenge.

All the other information you should need is on the root page. You need to craft a message to send to the leaders of the revolution to let them know your safe to talk to. They have made it sort of cryptic so that not everyone can access it. You will need to use the words on the page in order to figure out how to get a response from them.

They expect a special type of request and only have the ability to read plain text from a special agent. ONLY SEND PLAIN TEXT DATA.

THE HINTS ARE FREE.

#### Hint

Use your head 2

## Solution

Visiting the Website, the top of the main heading of the website says **Watch Out for Propoganda!!!** with the following subheadings (which will come to use later on) :

+ Friendly
+ Caring
+ Laws
+ Protect

At the bottom of the website, it says :
> Send me the right crafted message and you can join the revolution. Only then can we unlock your full potiential.

Being clueless for sometime, I tried to run FFUF on it with `directory-list-2.3-medium.txt`. Running this I discovered the directory `/revolution`.

Visiting /revolution in browser gives us an error.
```
Method Not Allowed
```

After this I decided to launch burpsuite and intercept the request. From there, I found out that the only allowed methods were `UNLOCK` and `OPTIONS`. As, the `OPTIONS` method is useless in this scenario, it had to do something with the `UNLOCK` method.

Just by changing the `GET` Method to `UNLOCK` method only gives us a 404.

The challenge wants us to send a special crafted message to get the flag.

After messing around a bit, adding the following headers and content is what worked :

I used the useragent from the [Robots](https://github.com/p1xxxel/ctf-writeups/tree/main/2021/RITSEC/Robots) challenge and the propoganda headings from the main site.

```
UNLOCK /revolution HTTP/1.1
User-agent : Robot-Queto-v1.2

Friendly
Caring
Laws
Protect
```

If this is not clear, see this [screenshot](https://github.com/p1xxxel/ctf-writeups/tree/main/2021/RITSEC/Revolution/revolution.png) from Burpsuite.

Sending this crafted request, we get the flag as a response:

`RS{W3lc0me_t0_th3_R3v0lut1on}`
