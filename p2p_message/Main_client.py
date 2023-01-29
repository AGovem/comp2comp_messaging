# server
import socket
import sys
import time

server = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080

server.bind((s_ip,port))
print("Port and ip succesfully bind :)")
time.sleep(1.5)
print("This is server's ip: ", s_ip)

server.listen(2)
conn, add = server.accept()
print("recived connection from ",add[0])
print('Connection Established. Connected From: ',add[0])

client = conn.recv(1024).decode()
print(client + "has connected")
conn.send(host_name.encode())

while True:
    msg = input("Me : ")
    conn.send(msg.encode())
    msg = conn.recv(1024)
    msg = msg.decode()
    print(client, ":", msg)