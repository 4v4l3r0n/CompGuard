# modules/baseline.py

import os

WHITELIST_FILE = "resources/whitelist.txt"

def load_baseline():
    if not os.path.exists(WHITELIST_FILE):
        return set()
    with open(WHITELIST_FILE, "r") as f:
        return set(line.strip() for line in f)

