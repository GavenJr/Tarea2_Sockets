#Integrantes:
#Alex Barrera
#Felipe Caro
#Gbriel Venegaz
#Sergio Zuñiga

import socket

#Crear socket TCP/IP
sockServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Anclar el socket al puerto 
direccion_server = ('localhost', 10000)
print('Comenzado escucha en {} puerto {}'.format(*direccion_server))
sockServidor.bind(direccion_server)

#Escuchando hasta un maximo de 5 conecciones
sockServidor.listen(5)

while True:
    #Esperando Coneccion
    print('Esperando coneccion')
    coneccionCliente, direccion_cliente = sockServidor.accept()

    print('Coneccion desde: ', direccion_cliente)
    #Recivir la informacion y retransmitirla
    while True:
        mensaje = coneccionCliente.recv(40)
        print('recibido: ', mensaje)
        if mensaje == "desconectar":
            break
        print('enviando al cliente...')
        coneccionCliente.sendall(mensaje)
    #Desconectar cliente
    print("Desconectado cliente")
    coneccionCliente.close()


