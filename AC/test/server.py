import json
import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',123)
server_socket.bind(server_address)
server_socket.listen(1)
print("Server is listening ")
client_socket,client_address = server_socket.accept()
print("Connection Established ")

obj = client_socket.recv(1024).decode()
data=json.loads(obj)
cipher=data['cipher']
key=data['key']

print("Received Cipher ",cipher)
text=""
idx=0
for i in cipher:
    shift=int(key[idx]) - int('0')
    char=chr((ord(i)-shift-ord('A'))% 26 + ord('A'))
    idx+=1
    text+=char

print("Encrypted text ",text)

server_socket.close()
client_socket.close()