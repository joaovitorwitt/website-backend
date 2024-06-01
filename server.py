import socket
import select


if __name__ == "__main__":
    listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    address_port = ("127.0.0.1", 8080)
    listener_socket.bind(address_port)
    
    # listen for connections, max 1
    listener_socket.listen(1)

    print(f"Server listening at {address_port[0]}:{address_port[1]}")

    # loop indefinitely to continuously check for new connections
    while True:
        read_ready_sockets, _, _, = select.select(
            [listener_socket], # list of items we want to check for read-readiness (just our socket)
            [], # list of items we want to check for write-readiness (not interested)
            [], # list of items we want to check for "exceptional" conditions (also not interested)
            0 # timeout of 0 seconds, makes the method call non-blocking
        )

        # if a value was returned then we have a connection to read from
        if read_ready_sockets:
            # select.select() returns a list of readable objects, so we will iterate but we only expect a single item
            for ready_socket in read_ready_sockets:
                client_socket, client_address = ready_socket.accept()

                # read up to 4096 bytes of data from the client socket
                client_message = client_socket.recv(4096)
                print(f"Client said: {client_message.decode('utf-8')}")

                # send a response to the client, a byte string
                client_socket.sendall(b"Welcome to the server")

                try:
                    client_socket.close()

                except OSError:
                    # client disconected
                    pass


