# RITSEC Hash

#### Category : CRYPTO
#### Points : 250 (56 solves)
#### Author : 1nv8rZim

## Challenge

Hmmm.. we found this hash along with a white paper explaining this custom hashing algorithm.

Can you break it for us?

hash : 435818055906

Flag should be submitted as RS{<cracked hash>}

Author: 1nv8rZim

Attachment : RITSEC\_HASH.pdf

#### Hints

> The red crosses in the hash diagram are addition

> Goal here is not to test ur hash cracking rigs, please use rockyou.txt. Solution should be first match and hopefully will be pretty recognizable

## Solution

Opening the PDF, we can see the hashing algorithm it uses. We just need to make a script that will take each work from `rockyou.txt`, hash it using this algorithm and check with the given hash `435818055906`. A sample hash is also given which makes it easier.

I wrote the following script :

```python
seed = "RITSEC"
seed1 = seed.encode('UTF-8').hex()
seed_byte = bytearray.fromhex(seed1)
temp = bytearray()
counter = 0
with open("rockyou.txt", 'r') as infile:
    for line in infile:
        counter = counter + 1
        msg = line
        msg_hex = msg.encode('UTF-8').hex()
        msg_byte = bytearray.fromhex(msg_hex)
        msg_byte.pop()
        for char in msg_byte:
            for i in range(0,13):
                temp.append((((seed_byte[2]^seed_byte[4])&seed_byte[5])+seed_byte[1]+(se
ed_byte[3]<<2)+char+i)%256)
                temp.append(seed_byte[0])
                temp.append((seed_byte[3]<<2)%256)
                temp.append((seed_byte[1]>>5)%256)
                temp.append((seed_byte[5]+seed_byte[0])%256)
                temp.append(seed_byte[3])
                seed_byte = temp
                temp = bytearray()
        if(seed_byte.hex() == '435818055906'):
            print(counter)
            print(msg)
```

Running this script, we get the word :

`invaderzim`

**NOTE : As the hash isn't too complex, it is normal to get collisions**

Wrapping it in RS{}, we get our flag:

`RS{invaderzim}`
