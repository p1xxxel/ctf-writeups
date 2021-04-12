# Sessions

### Category : Web
### Points : 100 (302 solves)
### Author : f1rehaz4rd

## Challenge

Find the flag.

http://34.69.61.54:4777

Author: f1rehaz4rd

## Solution

Visiting the Website, we see a login page. Viewing the source of the site, a comment can be seen saying 

> remove comment later: login iroh:iroh

Using these credentials, logging in to the website, we see it is a tribute website to Iroh along with their Bio and a link to the family tree.

Those links lead to no where so I intercepted the request by Burpsuite and we see that there is a parameter :

```
Cookie: sessiontoken=UlN7MG5seV9PbmVfczNzc2lvbl90b2szbn0=
```
Putting the value of sessiontoken in cyberchef, we see that it is a base64 encoded string and we get the flag.

`RS{0nly_One_s3ssion_tok3n}`
