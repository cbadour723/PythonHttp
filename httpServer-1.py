import socket

HOST = 'localhost'
PORT = 8080

def handle_request(conn):
    request = conn.recv(1024).decode()
    if not request:
        return
    filename = request.split()[1]
    try:
        with open(filename[1:], 'rb') as f:
            content = f.read()
        response = b'HTTP/1.1 200 OK\r\n\r\n' + content
    except FileNotFoundError:
        response = b'HTTP/1.1 404 Not Found\r\n\r\n'
    conn.sendall(response)
    conn.close()

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'Server listening on {HOST}:{PORT}...')
        while True:
            conn, addr = s.accept()
            print(f'Connected by {addr}')
            handle_request(conn)

if __name__ == '__main__':
    run_server()
