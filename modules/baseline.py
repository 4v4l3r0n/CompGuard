# modules/baseline.py

import os

BASELINE_FILE = "resources/baseline.txt"

def load_baseline():
    if not os.path.exists(BASELINE_FILE):
        return set()
    with open(BASELINE_FILE, "r") as f:
        return set(line.strip() for line in f)

