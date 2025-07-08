# Add every active process to whitelist.txt, skipping duplicates
import psutil
from modules.identify_proc import get_file_hash

existing = set()
try:
    with open("resources/whitelist.txt", "r") as f:
        for line in f:
            existing.add(line.strip())
except FileNotFoundError:
    print("Whitelist file not found.")
    pass

with open("resources/whitelist.txt", "a") as f:
    for proc in psutil.process_iter(['name', 'exe']):
        try:
            pname = proc.info['name']
            pexe = proc.info['exe']
            if pexe:
                phash = get_file_hash(pexe)
            else:
                phash = "N/A"
            record = f"{pname},{phash}"
            if record not in existing:
                f.write(record + "\n")
                existing.add(record)
        except Exception:
            continue