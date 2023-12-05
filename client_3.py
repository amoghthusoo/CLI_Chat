import socket as so
import threading as th

client_socket = so.socket()

print()
username = input("Enter username : ")
# ip_address = input("Enter IP Address : ")
ip_address = "localhost"
port = 9999

client_socket.connect((ip_address, port))
client_socket.send(username.encode())

print("Successfully Connected with Server.")
print("Start Messaging ...")

def send():
    while True:
        message = input()
        client_socket.send(message.encode())

def receive():
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

sending_thread = th.Thread(target=send)
sending_thread.start()

receiving_thread = th.Thread(target=receive)
receiving_thread.start()