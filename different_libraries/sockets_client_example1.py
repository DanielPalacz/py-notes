import socket

# Konfiguracja połączenia
HOST = "localhost"  # lub "127.0.0.1"
PORT = 9000 # port, na którym działa Twój serwer


# Tworzymy gniazdo TCP (IPv4, stream)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Połączenie z serwerem
    s.connect((HOST, PORT))
    print((HOST, PORT), "- Client connected to server")

    # Tworzymy zapytanie HTTP GET
    request = (
        "GET / HTTP/1.1\r\n"
        f"Host: {HOST}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    print((HOST, PORT), "- Client will send request to server.", s)
    # Wysyłamy zapytanie
    s.sendall(request.encode("utf-8"))

    # Socket kliencki sygnalizuje: "nie będę już nic wysyłał"
    # - bez tego Deadlock:
    s.shutdown(socket.SHUT_WR)

    print((HOST, PORT), "- Client just sent request to server.")

    # Odbieramy odpowiedź
    response = b""
    while True:
        print((HOST, PORT), "- Client will receive data from server.")
        data = s.recv(1024)
        print((HOST, PORT), "- Client received data from server.")
        if not data:
            print((HOST, PORT), "- Client stopped to receive data from server. Closing connection.")
            break
        response += data
        print(str(response))

# Wyświetlamy całą odpowiedź HTTP
# print(response.decode("utf-8"))
