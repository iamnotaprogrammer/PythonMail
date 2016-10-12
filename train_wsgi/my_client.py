from socket import socket

client = socket()
address = '127.0.0.1', 54670
print client.connect(address)
print client.send('Hello server')
print client.recv(1024)
client.close()

