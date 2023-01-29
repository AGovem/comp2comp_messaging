
# client
import socket, sys, time

server_socket = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

print("This is your ip address ", ip)
server_host = input('Enter friend\'s IP address:')
name = input('Enter Friend\'s name: ')
server_socket.connect((server_host, sport))
server_socket.send(name.encode())
server_name = server_socket.recv(1024)
server_name = server_name.decode()
print(server_name," has joined...")

while True:
    msg = server_socket.recv(1024).decode()
    print(server_name, " : ", msg)
    msg = input("Me : ")
    server_socket.send(msg.encode())
