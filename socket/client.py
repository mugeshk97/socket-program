import socket

c = socket.socket()


c.connect(('localhost', 9999 )) # server ip address
print(c.recv(1024).decode())
