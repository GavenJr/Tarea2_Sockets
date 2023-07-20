import socket

__author__ = ''
'''
Synchronous tcp server
'''

# For tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# To fix the address already in use issue
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to all the interfaces on port 8080
sock.bind(("127.0.0.1", 5800))
# Number of backlog clients
sock.listen(2)
print("Waiting for client....!")
while True:
   ## (client, (ip, port)) = sock.accept()
    ip,port = sock.accept()
    print('client connected with ip as {} and port {}'.format(ip, port))
   ## data = client.recv(2048)
    data = ip.recv(2048)
    while len(data):
        print(len(data))
        print("Client sent the data : {}".format(data))
        # client.send(data.upper())
        ip.send(data.upper())
        # data = client.recv(2048)
        data = ip.recv(2048)
    print("Client closed connection !!! :( ")
    #client.close()
    ip.close()


print("Closing the Socket!!")
sock.close()