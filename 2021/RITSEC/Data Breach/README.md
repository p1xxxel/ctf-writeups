# Data Breach

#### Category : Intel
#### Points : 175 (203 solves)
#### Author : t0uc4n

## Challenge

Oh no! Geno’s email was involved in a data breach! What was his password? Author: t0uc4n

## Solution

To check if Geno's email was involved in a data breach, first we need to find the email. In [Finding Geno](), we had found the LinkedIn profile. Visiting that Profile again and looking at the **About** section we see :

```
https://about.me/genoikonomov
Email: incogeno@gmail.com
Phone: 1 (845) 702-4914 
```

So, now we have the email. At first I tried looking on sites like [HaveIBeenPwned](https://haveibeenpwned.com) and other data breach search websites. It wasn't in them.

Searching `"incogeno@gmail.com"`, we get a website with a lot of credentials.

Searching for Geno's email in it we find that the leaked password is
```
StartedFromTheBottom!
```

We need to wrap the flag in RS{}. So our flag becomes:

`RS{StartedFromTheBottom!}`
