import threading
import time

# Funkcja, która będzie wykonywana przez wątek
def print_numbers(name):
    for i in range(5):
        print(f"Wątek {name}: {i}")
        time.sleep(1)

# Tworzymy wątki
thread1 = threading.Thread(target=print_numbers, args=("A",))
thread2 = threading.Thread(target=print_numbers, args=("B",))

# Uruchamiamy wątki
thread1.start()
thread2.start()

# Czekamy na zakończenie wątków
thread1.join()
thread2.join()

print("Wątki zakończone")
