import socket

s=socket.socket()
host="127.0.0.1"       #This is your Server IP!
port=5678
s.connect((host,port))
s.send(b"hello")
rece=s.recv(1024)
print("Received",rece)
s.close()