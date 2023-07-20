from socket import *
serverName = 'localhost'
serverPort = 8600
clientSocket = socket(AF_INET,SOCK_DGRAM)
#clientSocket = socket('localhost', socket.SOCK_DGRAM)
message = input("Input lowercase sentence : ")
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()