import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Hey, u are finally awake",
            timeout = 10
        )
        time.sleep(3600)