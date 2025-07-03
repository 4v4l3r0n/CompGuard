# modules/process_monitor.py

import psutil

class ProcessMonitor:
    def __init__(self, logger):
        self.logger = logger

    def check_processes(self):
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                info = proc.info
                if info['username'] not in ('SYSTEM', 'root'):
                    self.logger.log_event("ProcessMonitor",
                                          f"Process: {info['name']} (PID {info['pid']}) User: {info['username']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
