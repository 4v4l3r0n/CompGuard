# modules/process_monitor.py

import psutil
from modules.whitelist import load_whitelist
from modules.identify_proc import get_file_hash

class ProcessMonitor:
    def __init__(self, notifier):
        self.notifier = notifier
        self.whitelist = load_whitelist()

    def check_processes(self):
        for proc in psutil.process_iter(['pid', 'name', 'exe']): # Process bilgilerini al
            try:
                pname = proc.info['name']
                pexe = proc.info['exe']
                pid = proc.info['pid']
                if pexe:
                    phash = get_file_hash(pexe)
                else:
                    phash = "N/A"

                if (pname,phash) not in self.whitelist:
                    print(f"***Unexpected Process: {pname} (PID {pid})")
                    print(f"PATH: {pexe}")
                    print(f"HASH: {phash}")
                    self.notifier.show_notification("Warning: Unexpected Process",
                                                     f"NAME {pname}\nPID {pid}")
            except (psutil.NoSuchProcess):
                print("NoSuchProcess")
                continue
            except (psutil.AccessDenied):
                print("AccessDenied")
                continue
            except (FileNotFoundError):
                print("FileNotFoundError")
                continue