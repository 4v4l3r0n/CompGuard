# modules/process_monitor.py

import psutil
from modules.whitelist import load_baseline
from modules.identify_proc import get_file_hash

class ProcessMonitor:
    def __init__(self, notifier):
        self.notifier = notifier
        self.baseline = load_baseline()

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

                if pname not in self.baseline:
                    print(f"***Beklenmedik process: {pname} (PID {pid})")
                    print(f"PATH: {pexe}")
                    print(f"HASH: {phash}")
                    self.notifier.show_notification("Uyarı: Beklenmedik Process", f"NAME {pname}\nPID {pid}")
            except (psutil.NoSuchProcess):
                print("NoSuchProcess")
                continue
            except (psutil.AccessDenied):
                print("AccessDenied")
                continue
            except (FileNotFoundError):
                print("FileNotFoundError")
                continue