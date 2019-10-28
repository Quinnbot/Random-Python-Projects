from socket import *

serverName = "localhost"
serverPort = 1234

client = socket(AF_INET, SOCK_DGRAM)

message = input()

client.sendto(message.encode(), (serverName, serverPort))
modmessage, serverAddress = client.recvfrom(1024)

print(modmessage.decode())
client.close()
