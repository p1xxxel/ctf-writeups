# Library

#### Category : Easy
#### Points : 244 (38 solves)

## Challenge

https://tryhackme.com/jr/incognito1

## Solution

Doing a nmap scan on the IP, we see that there is only one port open i.e. port 80.

```
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-title: Admin Login |Library Management System
|_Requested resource was admin.php
```
Visiting the page, we see it is a standard login page.

Enumerating directories, we find an interesting directory at `/database`.

Visiting the directory, we can see it is a .sql file. Let's download and open it. From the table `users`, we retrieve the credentials `admin:admin123` and use it to login to the website.

In the dashboard, we see the number of books borrowed and the number of borrowers. Going to the `Books` section and clicking on any of the book, we can see that there is an option to upload `Book Image`.

Let's try and upload a [php reverse shell](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php). Change the IP to match your OpenVPN IP and setup a netcat listener at the port specified. We see that our reverse shell has succesfully been uploaded. Now we just need to activate it. From our earlier directory scan we know there is a `/assets`.

Visiting `/assets/img/php-reverse-shell.php` activates the reverse shell. 

Reading `/etc/passwd`, we see that there is another user `cirius`. Trying `password` as the password in `su cirius`, it works.

Doing a `sudo -l`, tells us that we can execute any command on the machine. Now we just escalate our priveleges with sudo su and read root.txt

```
cirius@incognito:/$ sudo -l
Matching Defaults entries for cirius on incognito:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User cirius may run the following commands on incognito:
    (ALL : ALL) ALL
cirius@incognito:/$ sudo su
root@incognito:/# cat /root/root.txt
```



