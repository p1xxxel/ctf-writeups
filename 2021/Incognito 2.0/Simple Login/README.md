# Simple Login

#### Category : Easy
#### Points : 84 (58 solves)

## Challenge

Challenge Link: https://incognito-web.herokuapp.com/

#### Hint

The admin has **put** additional **security** measures to protect the site.

## Solution

Visiting the page, we see a login panel with Sign In, Sign Up and Forgot Password features but the only thing that works is the Sign In feature.

<img src=https://github.com/p1xxxel/ctf-writeups/tree/main/2021/Incognito%202.0/simple_admin.png>

I tried putting in the credentials `admin:admin` which resulted in the page saying :

>You are not who you say to be, bcz he has put some extra measures to prevent this scenario

Initially when there was no hint, I couldn't figure it out but after the hint came showing "put" in bold, I knew I had to use `PUT` method instead of `POST`.

Intercepting the request and changing the method to PUT, we get the flag:

`ICTF{N0T_S0_S3Cur3d_853541}`
