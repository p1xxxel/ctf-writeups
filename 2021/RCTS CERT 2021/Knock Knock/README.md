# Knock Knock

#### Category : network
#### Points : 100 (93 solves)

## Challenge

We recently found a private SSH key that will allow us to login in the attached machine.

However, we can't seem to be able to login through SSH.

Can you help us out?

No brute force is required.

Flag format: flag{string}

Attachment : knock_knock.ova, id_rsa

## Solution

We are given a .ova file which we can import in Virtualbox and load it. Make sure to note down the location where you are storing the virtual hard drive.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Knock%20Knock/vdi_file_location.png)

But when we load it, it asks for the password.

So what I do to bypass it is create another virtual machine, use the .vdi file created while importing the lockedout ova image with a live linux iso. In this case I downloaded archlinux iso.

To do this, create a new vm and add the iso as bootable disk, select the vdi file from locked out as the virtual hard drive and then boot into the live environment.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Knock%20Knock/arch_vm.png)

When you do `lsblk`, the `/dev/sda1` is the boot partition and `/dev/sda2` is the file system.

You might have some errors while mounting `/dev/sda2` directly.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Knock%20Knock/mounting_error.png)

If you do get the same error, use this solution https://askubuntu.com/questions/766048/mount-unknown-filesystem-type-lvm2-member and `/dev/sda2` should be mounted correctly.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Knock%20Knock/mounted_correctly.png)

Going to the user's home directory at `/home/ctf`, we find the flag.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Knock%20Knock/getting_flag.png)

So the flag is `flag{kn0ck1ng_0n_d00rs_1s_p0l1t3}`