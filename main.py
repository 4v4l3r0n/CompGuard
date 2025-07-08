from modules.process_monitor import ProcessMonitor
from modules.notification import Notifier
import time

def main():
    print("CyberGuardian Running...")
    notifier = Notifier()
    process_monitor = ProcessMonitor(notifier=notifier)
    while(True):
        process_monitor.check_processes()
        time.sleep(10)

if __name__ == "__main__":
    main()
