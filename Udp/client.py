import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello from Client"

client.sendto(message.encode('utf-8'),('192.168.1.4',1234))

data, addr = client.recvfrom(4096)
print(str(data))
client.close()