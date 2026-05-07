import socket

# Tworzymy socket UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Wiążemy socket z adresem IP i portem
server_socket.bind(("0.0.0.0", 9003))

print("UDP serwer nasłuchuje na porcie 9003...")

while True:
    # recvfrom() zwraca dane i adres nadawcy
    data, addr = server_socket.recvfrom(1024)  # 1024 bajty max
    print(f"Odebrano od {addr}: {data.decode()}")

    # Możemy odesłać odpowiedź do tego samego nadawcy
    response = f"Otrzymałem: {data.decode()}"
    server_socket.sendto(response.encode(), addr)
