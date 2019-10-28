from socket import *
import os.path
import threading

def request(connection ,inrequest):
     message = inrequest.split("/")
     message = message[1].split(" ")
     htmlfile = message[0]
     print("-------------------------------")
     print("request for: "+ htmlfile)

     connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
     if os.path.exists(htmlfile):
          print("sending")
          with open(htmlfile, 'r') as file:
               connectionSocket.send(file.read().encode())
     else:
          connectionSocket.send("404 not found".encode())

     connectionSocket.close()
     print("-------------------------------")



serverPort = 1234
serverSocket = socket(AF_INET , SOCK_STREAM)
serverSocket.bind(('' , serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
     try:
          connectionSocket, addr = serverSocket.accept()
          message = connectionSocket.recv(1024).decode()
     except:
          print("connection failed")

     if(not(".ico" in message)):
          thread = threading.Thread(target=request, args=(connectionSocket, message))
          thread.start()
