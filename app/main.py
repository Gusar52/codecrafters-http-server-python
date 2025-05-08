import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    


    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    client_socket, addr = server_socket.accept()

    with client_socket:

        data = client_socket.recv(1024)

        request = data.decode()

        print(request)

        # Parse the HTTP request

        if request.startswith("GET / HTTP/1.1"):

            response = "HTTP/1.1 200 OK\r\n\r\n"

        else:

            response = "HTTP/1.1 404 Not Found\r\n\r\n"

        client_socket.sendall(response.encode())

        # client_socket.sendall(data)


if __name__ == "__main__":
    main()
