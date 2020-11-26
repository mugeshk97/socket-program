import socket

sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.bind((socket.gethostbyname(socket.gethostname()), 1234)) 
sever.listen(3) 

print("server waiting for connection")
payload = 'Hey client'

while True:
	client, address = sever.accept()
	print("connected with ", address)
	while True:
		data = client.recv(1024)
		if not data:
			break
		print('data recieved from client :', data.decode('utf-8'))
		try:
			client.send(bytes(payload, "utf-8"))
		except:
			print("exited by user")
	client.close()
sever.close()