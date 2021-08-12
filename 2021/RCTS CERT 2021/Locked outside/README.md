# Locked Outside

#### Category : mission, boot2root
#### Points : 100 (66 solves)

## Challenge
Based on the payload discovered, the employee’s computer was used to compromise a machine in our network.

We checked the machine and confirmed that we’ve lost SSH access to it.

Can you check if we can get the access back?

Flag format: flag{string}

Attachment : [lockedout.ova](https://defendingthesoc.ctf.cert.rcts.pt/files/c38e9686867c3632cdbea043d840e4fa/lockedout.ova?token=eyJ1c2VyX2lkIjoyOTAsInRlYW1faWQiOjEzMSwiZmlsZV9pZCI6MzF9.YRSdJQ.wRkc0EPi9ExkzpVPcnAjxQnxKs0)

## Solution
We are given a .ova file which we can import in Virtualbox and load it. Make sure to note down the location where you are storing the virtual hard drive.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Locked%20outside/vdi_file_location.png)

But when we load it, it asks for the password.

So what I do to bypass it is create another virtual machine, use the .vdi file created while importing the lockedout ova image with a live linux iso. In this case I downloaded archlinux iso.

To do this, create a new vm and add the iso as bootable disk, select the vdi file from locked out as the virtual hard drive and then boot into the live environment.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Locked%20outside/arch_vm.png)

When you do `lsblk`, the `/dev/sda1` is the boot partition and `/dev/sda2` is the file system.

You might have some errors while mounting `/dev/sda2` directly.
![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Locked%20outside/mounting_error.png)

If you do get the same error, use this solution https://askubuntu.com/questions/766048/mount-unknown-filesystem-type-lvm2-member and `/dev/sda2` should be mounted correctly.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Locked%20outside/mounting_file_system.png)

The problem description says to get back the ssh connection so I checked `/etc/ssh/sshd_config` and we find the flag.

![](https://github.com/p1xxxel/ctf-writeups/blob/main/2021/RCTS%20CERT%202021/Locked%20outside/finding_flag.png)
