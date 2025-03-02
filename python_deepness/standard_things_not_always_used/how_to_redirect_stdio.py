import dis
import io
import sys

def f(x):
    return x * 2

# Tworzymy obiekt StringIO do przechwycenia outputu
output = io.StringIO()

# Przekierowanie standardowego wyjścia
sys.stdout = output
dis.dis(f)
sys.stdout = sys.__stdout__  # Przywracamy normalne wyjście

# Zapisujemy wynik do zmiennej
dis_output = output.getvalue()

print("Zawartość zmiennej:")
print(dis_output)
