from socket import *
import keyboard

keyboard.add_hotkey('ctrl+shift+/', lambda: closeserver())

serverName = "10.220.27.13"
serverPort = 1234

server = socket(AF_INET, SOCK_DGRAM)

server.bind(('',serverPort))

print("server is ready")

while True:
    modmessage, clientAddress = server.recvfrom(1024)
    modmessage = modmessage.decode().upper()
    print("recived: " + modmessage)
    server.sendto(modmessage.encode(), clientAddress)


def closeserver():
    print("closing server")
    server.close()
    exit()
