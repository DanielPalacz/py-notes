import debugpy
from psutil import Process

# Otwórz port 5678 dla połączenia z debuggerem
debugpy.listen(("localhost", 5678))

print("Czekam na połączenie z IDE...", "Process:", Process().pid)

# Zatrzymaj kod do czasu połączenia debuggerem
debugpy.wait_for_client()
debugpy.breakpoint()

# Tu następuje normalny kod do debugowania
x = 10
y = 20
z = x + y
print(f"Wynik: {z}")
