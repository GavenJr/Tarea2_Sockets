#Integrantes:
#Alex Barrera
#Felipe Caro
#Gabriel Venegaz
#Sergio Zuñiga

import socket

#Creamos el Socket TCP del cliente
sServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Establecemos la direccion del servidor
direccion_server = ('localhost', 8000)
print('Comenzando en {} puerto {}'.format(*direccion_server))
sServidor.bind(direccion_server)

#Estbalecemos el maximo de clientes que peude atender el Servidor
sServidor.listen(5)

while True:
    #Esperamos una conexion
    print('Esperando una conexion...')
    #Aceptamos la conexion
    cliente, direccion = sServidor.accept()
    print('Conexion establecida con: ', direccion)

    while True:
        #Recibimos e imprimos el mensaje en el servidor
        mensaje = cliente.recv(1024).decode()
        print('Recibido: ', mensaje)

        #Verificamos si el mensaje fue "desconectar"
        if mensaje == "desconectar": 
            print("Desconectando cliente")
            break

        #Enviamos el mesnaje de vuelta al cliente
        cliente.sendall(mensaje.encode()) 

    #Cerramos la coneccion entre el cliente y el servidor
    cliente.close()
    print("Conexión cerrada con el cliente")