import threading
import time

# Funkcja, która czeka na sygnał
def wait_for_event(event):
    print("Wątek czeka na sygnał...")
    event.wait()  # Czeka, aż event zostanie ustawiony
    print("Wątek wznowił działanie!")

# Tworzymy Event
event = threading.Event()

# Tworzymy wątek
thread = threading.Thread(target=wait_for_event, args=(event,))

# Uruchamiamy wątek
thread.start()

# Symulacja jakiegoś opóźnienia w głównym wątku
time.sleep(2)

# Ustawiamy event, aby wznowić działanie wątku
print("Główny wątek wysyła sygnał do wątku!")
event.set()

# Czekamy na zakończenie wątku
thread.join()
