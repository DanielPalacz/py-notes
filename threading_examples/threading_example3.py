import threading

# Zmienna współdzielona
counter = 0
lock = threading.Lock()

# Funkcja, która będzie modyfikować współdzieloną zmienną
def increment():
    global counter
    for _ in range(1000000):
        # Blokujemy dostęp do zmiennej, aby uniknąć problemów
        with lock:
            current_thread = threading.current_thread().name
            print(current_thread)
            counter += 1

# Tworzymy wątki
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Uruchamiamy wątki
thread1.start()
thread2.start()

# Czekamy na zakończenie wątków
thread1.join()
thread2.join()

print(f"Wartość countera: {counter}")
