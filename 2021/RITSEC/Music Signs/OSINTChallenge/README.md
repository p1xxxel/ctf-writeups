# OSINTChallenge

#### Category : Intel
#### Points : 250 (112 solves)
#### Author : FrozenTundras

## Challenge

The CEO of Geno’s company loves local art and nature. Where was she when she took the photo in her Twitter background? (Wrap the answer in RS{} and use underscores between each word.)

Author: FrozenTundras

## Solution

First we need to find the name of the CEO. Searching for `CEO Bridgewater Investigation`, we get the second result as a LinkedIn Profile saying :

```
Dr. JoAnne Turner-Frey
Chief Executive Officer at Bridgewater Investigations
Rochester, New York, United States 
```

Now we need to find her on twitter. Going to twitter and searching for `JoAnne Turner-Frey`, we find her profile. According to the challenge, we need to find which place the Twitter background is from.

I tried reverse image searching but did not find anything meaningful but if we see the challenge description carefully, it says

> The CEO of Geno’s company loves local art and nature.

Also from her Twitter Bio,

> Rochesterian since '04

From this I concluded that this place is probably somewhere in Rochester NY. Also we can see in the Twitter Background that it is a Peace symbol.

Opening [Google Maps](maps.google.com), I typed in Rochester NY and pressed enter. After that I clicked on `Nearby` to search for nearby places. Then I type peace sign which gave me a result of 
```
Peace Sign Garden Durand Eastman Park
```

The challenge asked us for the place so our flag becomes:
`RS{Durand_Eastman_Park}`
