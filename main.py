from modules.process_monitor import ProcessMonitor
from modules.notification import Notifier

def main():
    print("CyberGuardian Başlatıldı.")
    notifier = Notifier()


    process_monitor = ProcessMonitor(
        notifier=notifier
    )
    process_monitor.check_processes()

if __name__ == "__main__":
    main()
