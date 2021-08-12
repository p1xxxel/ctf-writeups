# Changing our locks and dumping old keys

#### Category : mission, reverse
#### Points : 100 (56 solves)

## Challenge
There should be something in the server that was used to maintain persistence.

Can you track this one and find more information about the attacker?

Flag format: flag{string}

## Solution
This is continuation of `Locked outside` so I assume if you have access to the machine.

It says to find more information about what was used to maintain persistence.

The `home` directory was empty so I went into the `root` directory and there were the following files.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Changing%20our%20locks%20and%20dumping%20old%20keys/root_dir.png)

`.ash_history` is useless as it is a symlink to `/dev/null` but `.viminfo` is 11k size.

Reading `.viminfo`, we find the flag in the first few lines.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Changing%20our%20locks%20and%20dumping%20old%20keys/finding_flag.png)
