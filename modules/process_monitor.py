# modules/process_monitor.py

import psutil
from modules.baseline import load_baseline

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

                if pname not in self.baseline:
                    msg = f"Beklenmedik process: {pname} (PID {pid})"
                    self.notifier.show_notification("Uyarı: Beklenmedik Process", msg)

            except (psutil.NoSuchProcess, psutil.AccessDenied, FileNotFoundError):
                continue
