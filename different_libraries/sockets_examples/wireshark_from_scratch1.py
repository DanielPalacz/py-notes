import socket

sock = socket.socket(
    socket.AF_PACKET,
    socket.SOCK_RAW,
    socket.ntohs(3)
)

while True:
    data, address = sock.recvfrom(65535)
    print(f"Odebrano {len(data)} bajtów z {address}")
