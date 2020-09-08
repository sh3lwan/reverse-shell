import socket
import sys

server_address = '';
print(server_address)
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (server_address, 10000)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            print("Server>", end=" ")
            cmd = input()

            if(cmd == 'quit'):
                sock.close()
                connection.close()
                sys.exit()

            if(len(str.encode(cmd)) > 0):
                connection.send(str.encode(cmd))
                client_response = str(connection.recv(1024), 'utf-8')
                print(client_response, end="\n")
    finally:
        # Clean up the connection
        print("Closing current connection")
        connection.close()