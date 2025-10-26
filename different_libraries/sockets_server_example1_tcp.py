import socket
import threading


def handle_connection(c_socket, c_address):
    print("[handle_connection thread][function execution start] - Thread space.")
    print('[handle_connection thread] Connected by:', c_address)

    with c_socket:
        while True:
            data = c_socket.recv(1024)
            if not data:
                break

            c_socket.sendall(b"Bytes from server... 1.")
            print("[handle_connection thread][function execution] while loop end.")
            break

        print('[handle_connection thread][c_socket end]', c_address)

    print("[handle_connection thread][function execution end]")


# Konfiguracja połączenia
HOST = "localhost"  # lub "127.0.0.1"
PORT = 9003  # port, na którym działa Twój serwer
SERVER_ADDRESS = (HOST, PORT)

# create an INET, STREAMing socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(SERVER_ADDRESS) # bind the socket to a well-known port
server_socket.listen() # become a server sock



while True:
    # accept connections from outside
    print("[Server main loop][global scope][start] waiting for connections from outside.", SERVER_ADDRESS)
    (client_socket, s_address) = server_socket.accept()
    print("[Server main loop][global scope][start] new connection was accepted by server.", SERVER_ADDRESS, client_socket)

    # now do something with the client_socket
    # in this case, we'll pretend this is a threaded server
    # ct = make_client_thread(client_socket)

    # client_socket.settimeout(5)
    cst = threading.Thread(target=handle_connection, args=(client_socket, s_address))
    cst.start()

    print("[Server main loop][global scope][end] end.", SERVER_ADDRESS)
