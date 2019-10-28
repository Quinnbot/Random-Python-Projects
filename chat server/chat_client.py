from socket import *
import threading

serverip = input("please enter the ip of the server: ")
serverport = int(input("please enter the port of the server"))

client = socket(AF_INET, SOCK_DGRAM)

client.sendto("{new}".encode(), (serverip, serverport))
modmessage, serverAddress = client.recvfrom(1024)
print(modmessage.decode())
client.sendto("quinn".encode(), (serverip, serverport))
#modmessage, serverAddress = client.recvfrom(1024)