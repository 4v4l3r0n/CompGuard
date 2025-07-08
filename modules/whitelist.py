import os

WHITELIST_FILE = "resources/whitelist.txt"

def load_whitelist():
    whitelist = set()
    if not os.path.exists(WHITELIST_FILE):
        print("Whitelist file not found. Using empty whitelist.")
        return whitelist
    with open(WHITELIST_FILE, "r") as f:
        for line in f:
            pname,phash = line.strip().split(",",1)
            whitelist.add((pname, phash))
        return whitelist

