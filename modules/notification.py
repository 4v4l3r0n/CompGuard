# modules/notification.py

from winotify import Notification

class Notifier:
    def __init__(self):
        pass

    def show_notification(self, title, message):
        toast = Notification(app_id="CyberGuardian",
                             title=title,
                             msg=message,
                             duration="short")
        toast.show()
