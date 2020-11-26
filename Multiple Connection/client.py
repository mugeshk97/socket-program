import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'ip address of server'
port = 1234

print("waiting for server")

try:
    client.connect((host,port))
except socket.error as e:
    print(e)

while True:
    payload = input("Enter Message : ")
    client.send(bytes(payload, 'utf-8'))
    response = client.recv(2048)
    print(f'From Server : ',response.decode('utf-8'))
client.close()