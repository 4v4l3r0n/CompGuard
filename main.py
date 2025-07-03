# main.py

import sys
from modules.logger import Logger
from modules.process_monitor import ProcessMonitor

def main():
    print("CyberGuardian Başlatıldı.")
    logger = Logger()
    logger.log_event("main", "Uygulama başlatıldı.")

    process_monitor = ProcessMonitor(logger)
    process_monitor.check_processes()

    logger.close()


if __name__ == "__main__": 
    main()
