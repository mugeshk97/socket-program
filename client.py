import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('ip of server', 1234)) # server ip address
payload = 'Hey server'

try:
    while True:
        client.send(payload.encode('utf-8'))
        data = client.recv(1024).decode('utf-8')
        print('data from server, ', data)
        payload = input("enter the payload")

except KeyboardInterrupt:
    print("exited")
client.close()