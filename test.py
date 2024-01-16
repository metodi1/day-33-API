import socket

host = "xxx.xxx.xxx.xxx"  # Replace with the actual IP address
port = 12345  # Replace with the actual port

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        # Your code for communication with the server goes here
except socket.error as e:
    print(f"Socket connection failed: {e}")