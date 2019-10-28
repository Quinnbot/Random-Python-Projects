from socket import *
import threading


clients = []


def sendMSG(name, num, message):

     for x in range(len(clients)):
          if(not x == clientNum):
               clients[x].send(clients[x] +": "+message.encode())



def newClient(connection):
     print("got here")
     connection.send("please enter your screen name!".encode())
     name = connection.recv(1024).decode()

     while(name in clients):
          connection.send("thats already taken! please try again!".encode())
          name = connection.recv(1024).decode()

     msg = name + "has joined the server."
     sendMSG(-1, msg)#-1 to send to everyone
     clients.append(connection)

     thread = threading.Thread(target=listen, args=(name, len(clients)-1, connection))
     thread.start()




def closeConnection(name, num):

     msg = name + "has left the server."
     sendMSG(clientNum, msg)

     clients[clientNum].close()
     clients.pop(clientNum)



def listen(name, num, connection):

     while True:

          message = connection.recv(1024).decode()

          if(message == "{quit}"):
               closeConnection(name, num)
               break

          else:
               sendMSG(name, num, message)


serverPort = 1234
serverSocket = socket(AF_INET , SOCK_STREAM)
serverSocket.bind(('' , serverPort))
serverSocket.listen(1)

print('The server is ready to receive')
while True:

     try:
          connectionSocket, addr = serverSocket.accept()
          message = connectionSocket.recv(1024).decode()

          if(message == "{new}"):
               clientNum = clients.index(message)
               connectionSocket.send("101: recived")
               thread = threading.Thread(target=newClient, args=(connectionSocket))
               thread.start()

     except:
          print("connection failed")

