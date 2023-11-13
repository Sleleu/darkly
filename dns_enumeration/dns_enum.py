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