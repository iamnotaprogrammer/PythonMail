from socket import socket

client = socket()
address = '127.0.0.1', 54670
client.connect(address)
print client.send(b'Hello server')
print client.recv(1024)
client.close()

