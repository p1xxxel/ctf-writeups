# Robots

### Category : Web
### Points : 100 (500 solves)
### Author : f1rehaz4rd

## Challenge

Robots are taking over. Find out more.

34.69.61.54:5247

Author: f1rehaz4rd

## Solution

Visiting the Website, we see the title as **Robots are Taking Over** and content of the webpage saying 

> You need to hide. They have become smarter than us.

From the name, I decided to visit /robots.txt.

Here there are 2 interesting things :
* User-agent: Robot-Queto-v1.2 (which was useful in the next web challenge)
* Allow: /flag/UlN7UjBib3RzX2FyM19iNGR9

Visiting the second url, gives us a **Not Found** Error.

Putting the last portion of the url i.e. `UlN7UjBib3RzX2FyM19iNGR9` in cyberchef, it turns out it was a Base64 encoded string and we get the flag :

`RS{R0bots_ar3_b4d}`
