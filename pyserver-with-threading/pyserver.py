from socket import *
import os.path

serverPort = 1234
serverSocket = socket(AF_INET , SOCK_STREAM)
serverSocket.bind(('' , serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
     connectionSocket, addr = serverSocket.accept()
     message = connectionSocket.recv(1024).decode()

     print("request received")

     message=  message.split("/")
     message = message[1].split(" ")
     htmlfile = message[0]

     connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
     if os.path.exists(htmlfile):
          with open(htmlfile, 'r') as file:
               connectionSocket.send(file.read().encode())
     else:
          connectionSocket.send("404 not found".encode())

     print("reply sent")
     connectionSocket.close()
