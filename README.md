# Remote Shell Application

This project consists of a simple client-server architecture that allows a server to execute commands on connected clients remotely. The implementation is done using Python's `socket` and `threading` modules to enable multiple client connections.

## Features
- Accepts multiple client connections.
- Allows the server to list connected clients.
- Executes shell commands remotely on connected clients.
- Supports changing directories remotely.
- Securely disconnects from clients when needed.

## Installation and Usage

### Prerequisites
- Python 3.x installed on both server and client machines.

### Server Setup
1. Clone the repository or copy the script.
2. Run the server script on the host machine:
   ```bash
   python server.py
   ```
3. The server will start listening on `PORT 5555` (you can change it in the script).
4. When a client connects, it will be added to the list of available clients.
5. Use the `list` command to view connected clients.
6. Select a client and send commands.

### Client Setup
1. Run the client script on the target machine:
   ```bash
   python client.py
   ```
2. The client will attempt to connect to the server at `127.0.0.1:5555` (change it in the script if needed).
3. Once connected, the server can execute commands remotely on the client.

## Commands
| Command | Description |
|---------|-------------|
| `list` | Lists all connected clients |
| `cd <dir>` | Changes directory on the client machine |
| `<any shell command>` | Executes the given shell command on the client |
| `exit` | Disconnects from the current client |

## Notes
- The server must be running before clients can connect.
- Commands executed on the client machine are processed using `subprocess`.
- Ensure proper firewall settings to allow communication over the specified port.
- This tool should only be used in environments where remote execution is authorized and controlled.

## Disclaimer
This project is for educational purposes only. Use it responsibly and ensure you have permission before remotely accessing any system.
