import socket

HOST = input('Enter server IP address: ')
PORT = int(input('Enter server port number: '))

filename = input('Enter file path: ')
request = f'GET /{filename} HTTP/1.1\r\nHost: {HOST}\r\n\r\n'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(request.encode())
    response = b''
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data
    print(response.decode())
