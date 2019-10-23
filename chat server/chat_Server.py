from socket import *
import threading


clients = []


def sendMSG(connection, inrequest, ignoreClient):

     connectionSocket.send(inrequest.encode())
     connectionSocket.close()



serverPort = 1234
serverSocket = socket(AF_INET , SOCK_STREAM)
serverSocket.bind(('' , serverPort))
serverSocket.listen(1)

print('The server is ready to receive')
while True:
     print("ok")
     try:
          connectionSocket, addr = serverSocket.accept()
          message = connectionSocket.recv(1024).decode()

          if("" in clients):
               thread = threading.Thread(target=sendMSG, args=(connectionSocket, message))
               thread.start()

     except:
          print("connection failed")

     thread = threading.Thread(target=sendMSG, args=(connectionSocket, message))
     thread.start()