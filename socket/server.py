import socket

s = socket.socket()
print("socket created")
# we need to accept the connection so we need to specify the ip and port number
s.bind(('localhost', 9999))
#start listening to the client
s.listen(3) # num of connection that can listen
print("waiting for connections")

#to accept the connection 
while True:
	c, address = s.accept()
	print("connected with ", address)

	c.send(bytes("Response from server", "utf-8"))
	c.close()
