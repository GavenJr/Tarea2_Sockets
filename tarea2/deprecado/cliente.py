#Integrantes:
#Alex Barrera
#Felipe Caro
#Gbriel Venegaz
#Sergio Zuñiga

import socket

#Crear socket TCP/IP
sockCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conectar el socket al puerto donde esta haciendo escucha el servidor
direccion_server = ('localhost', 10000)
print('conectando a {} puerto {}'.format(*direccion_server))
sockCliente.connect(direccion_server)

mensaje = " "

while mensaje != "desconectar":
    mensaje = input("Escriba el mensje a enviar: ")
    sockCliente.sendall(mensaje)
    #Recibe mensaje del servidor (eco)
    recibido = sockCliente.recv(40)
    #Imprime mensaje recibido
    print(recibido)

#Se envio un desconectar
print('cerrando socket')
sockCliente.close()