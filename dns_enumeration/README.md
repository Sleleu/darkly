### Challenge

We have credentials, but it's impossible to enter them either in the signin area or in the VM.
That's fortunate because I wanted to enumerate the site for a while in search of leads. So, I created this script:

```python
#!/bin/python3

import requests
import argparse
from urllib.parse import urljoin
from signal import signal, SIGINT

YELLOW = "\033[1;33m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_GREEN = "\033[1;32m"
END = "\033[0m"

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.usage = "./dns_enum.py [-hw] URL"
    parser.add_argument("-w", "--wordlist", required=True, help="indicates the wordlist file to use for DNS enumeration.")
    parser.add_argument("URL", help="URL to enum")
    return (parser.parse_args())

def getWordlist(arg: str) -> list:
    try:
        with open(arg) as file:
            wordlist: list = file.read().splitlines()
    except:
        print(f"{YELLOW}\nCannot open file: {arg}{END}\n")
        exit(1)	
    return wordlist

def signalHandler(signum, _):
	if signum == SIGINT:
		print("")
		exit(0)

def getResponse(url: str) -> bool:
    try:
        response = requests.get(url)
        if "404 Not Found" not in response.text:
            print(f"{LIGHT_CYAN}Found:{END} {LIGHT_GREEN}{url}{END}")
    except:
        print(f"Spider: cannot get a response from url: {url}")
        exit(1)

def dns_discover(url: str, wordlist: list):
    for word in wordlist:
        full_url = urljoin(url, word)
        getResponse(full_url)

if __name__ == "__main__":
    signal(SIGINT, signalHandler)
    args = parse_arguments()
    url = args.URL
    wordlist = getWordlist(args.wordlist)
    dns_discover(url, wordlist)
```

I used one of the enumeration lists from the famous SecList: https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS

When running it, it provides me with the following results:

```
darkly ./dns_enum.py http://192.168.56.107/ -w subdomains-top1million-5000.txt 
Found: http://192.168.56.107/admin
Found: http://192.168.56.107/images
Found: http://192.168.56.107/css
Found: http://192.168.56.107/js
Found: http://192.168.56.107/audio
```

Well, of course, /admin...

Going there, we come across an authentication page, so I imagine we can enter the obtained credentials here, namely root:qwerty123@

And there you go!

```
The flag is: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
```

### Vulnerability

This folder was mentionned in the robots.txt. The file robots.txt is used to give instructions to web robots, such as search engine crawlers, about locations within the web site that robots are allowed, or not allowed, to crawl and index.

The presence of the robots.txt does not in itself present any kind of security vulnerability. However, it is often used to identify restricted or private areas of a site's contents.
Here, the htpasswd file is directly accessible by the web server, which is a vulnerability. This file is used to store the credentials needed to administer the web server.

### How to prevent from this vulnerability

Like the file_searching challenge: 
- Do not rely on robots.txt to provide any kind of protection over unauthorized access
- Not assume that all web robots will honor the file's instructions
- Use the file htaccess to protect the htpasswd :
	```
 	AuthType Basic
	AuthName "restricted area"
	AuthUserFile /path/to/the/directory/you/are/protecting/.htpasswd
	require valid-user
 	```

### Resources
- https://stackoverflow.com/questions/5229656/password-protecting-a-directory-and-all-of-its-subfolders-using-htaccess
- https://portswigger.net/kb/issues/00600600_robots-txt-file
- https://htaccessbook.com/protect-htaccess-files/
- https://filemanagerpro.io/article/how-to-deny-access-to-files-folders-through-htaccess-file/
