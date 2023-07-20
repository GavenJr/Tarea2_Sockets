__author__ = ''
import socket
received = "sin conexión"


######    sock = socket.socket()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = input()
try:
    #sock.connect(("localhost", 9999), )
    sock.connect(("127.0.0.1", 5800), )
   ### sock.sendall(data + '\n')
    sock.sendall(data.encode())
    received = sock.recv(1024)
except Exception as e:
    print(e)

finally:
    sock.close()

print('Sent data :{} '.format(data))
print("Received  data :{} ".format(received))