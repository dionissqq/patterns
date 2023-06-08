import socket
import threading

# Server
class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        # Create a server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

        print(f"Server listening on {self.host}:{self.port}")

        while True:
            # Accept incoming client connections
            client_socket, client_address = self.server_socket.accept()
            print(f"New client connected: {client_address}")

            # Handle client requests in a separate thread
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        # Receive and process client requests
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            # Process the request (echo back the message)
            response = data.decode("utf-8")
            client_socket.sendall(response.encode("utf-8"))

        # Close the client socket
        client_socket.close()


# Client
class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def connect(self):
        # Create a client socket and connect to the server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

    def send_message(self, message):
        # Send a message to the server and receive the response
        self.client_socket.sendall(message.encode("utf-8"))
        response = self.client_socket.recv(1024).decode("utf-8")
        print(f"Server response: {response}")

    def disconnect(self):
        # Close the client socket
        self.client_socket.close()


# Usage
if __name__ == '__main__':
    # Start the server
    server = Server("localhost", 3001)
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    # Connect a client and send a message
    client = Client("localhost", 3001)
    client.connect()
    client.send_message("Hello, server!")

    # Disconnect the client
    client.disconnect()

    # Wait for the server thread to finish
    server_thread.join()
