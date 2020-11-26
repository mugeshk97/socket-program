import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 1234

try:
    server.bind((host, port))
except socket.error as e:
    print(e)

print('waiting for connection')
server.listen(5)

def client_thread(client):
    client.send(bytes("Msg From Server", 'utf-8'))
    while True:
        data = client.recv(2048)
        print('From client : ',data.decode('utf-8'))
        payload = bytes("Hello I am server", 'utf-8')
        if not data:
            break
        client.send(payload)
    client.close()

while True:
    client, address = server.accept()
    print(f'connected to ip {address[0]} port {address[1]}')
    x = threading.Thread(target=client_thread,args=(client,))
    x.start()
    print(f"thread {threading.activeCount() - 1}")
server.close() 