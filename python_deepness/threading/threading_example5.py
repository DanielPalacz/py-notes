import threading
import time

# W Pythonie wątek daemon (demon) to wątek, który nie blokuje zakończenia procesu.


def monitor():
    while True:
        print("Sprawdzam stan systemu...")
        time.sleep(5)


monitor_thread = threading.Thread(
    target=monitor,
    daemon=True,
)

monitor_thread.start()

# Główna część programu
time.sleep(11)
print("Koniec programu")
