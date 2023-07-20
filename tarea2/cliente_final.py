#Integrantes:
#Alex Barrera
#Felipe Caro
#Gabriel Venegaz
#Sergio Zuñiga

import socket

#Creamos el socket CLiente TCP
sCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conectamos el cliente al servidor con los datos del servidor
direccion_server = ('localhost', 8000)
print('Conectando a {} puerto {}'.format(*direccion_server))
sCliente.connect(direccion_server)

mensaje = " "

#Iniciamos un bucle hasta que el cliente envie el mensjae "desconectar"
while mensaje != 'desconectar':

    mensaje = input('Escriba el mensaje a enviar: ')

    #verificamos la longitud del mensaje
    if len(mensaje) > 200: 
            print('l mensaje no puede superar los 200 caracteres.')
            continue

    #Enviamos el mensaje al servidor
    sCliente.sendall(mensaje.encode())

    #Esperamos la respuesta del servidor
    recibo = sCliente.recv(1024).decode()
    print('Mensaje recibido: ', recibo)

#Al escibir "desconectar" se sale del cilo una vez enviado el mensaje
# y se cierra el Socket del cliente
print('Cerrando Socket')
sCliente.close()