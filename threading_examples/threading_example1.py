import threading
import time

# Funkcja, która będzie wykonywana przez wątek
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)  # Opóźnienie na 1 sekundę

# Tworzymy wątek
thread = threading.Thread(target=print_numbers)

# Uruchamiamy wątek
thread.start()

# Czekamy na zakończenie wątku
thread.join()

print("Wątek zakończony")
