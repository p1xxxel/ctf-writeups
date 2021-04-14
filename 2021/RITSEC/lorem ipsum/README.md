# lorem ipsum

#### Category : CRYPTO
#### Points : 150 (135 solves)
#### Author : raydan

## Challenge

Flag is case sensitive.

author: raydan

Attachments :
+ cipher.txt
+ hint.jpg

## Solution

Putting the given cipher text in [cipher identifier](https://www.dcode.fr/cipher-identifier), we get that the name of the cipher is `Trithemius Ave Maria`.

When we try to decrypt it, it gives us :

`RSTHISISTRITHEMIUS`

But this is not the final flag as the challenge says, it is case sensitive.

Changing the case sensitivity as per the given `cipher.txt`(If the case of the starting alphabet of the word is uppercase, we change the decypted alphabet to upper case as well).

By this change and and wrapping it with {}, we get:

`RS{ThIsIsTrItHeMiUs}`


