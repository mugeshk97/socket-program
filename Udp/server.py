import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((socket.gethostbyname(socket.gethostname()), 1234))

while True:
    data, addr = server.recvfrom(4096)
    print(data.decode('utf-8'))
    message = bytes("Hello from UDP server", 'utf-8')
    server.sendto(message, addr)