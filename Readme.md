<!-- This content will not appear in the rendered Markdown -->
<!-- Los comentarios se hacen usando sintaxis HTML -->
<!-- -->

# Tarea Nro.2 Sockets

##  Comunicacion cliente-Servidor

### Grupo por: 

1. Alex Barrera
2. Felipe Caro
3. GavenJr
4. Sergio Zuñiga

#### El codigo fuente se encuentra bajo "Tarea2_Sockets/tarea2/"
ignorar las carpetas /ref y /deprecado

<p align="center" width="100%">
    <img width="100%" src="https://images.ctfassets.net/3prze68gbwl1/asset-17suaysk1qa1jhj/bf547110b07a076c30bac70e1b5a7e9a/python-socket-connection-diagram.png">
</p>

- - -


<details><summary>Como correr</summary>
<p>

Importar a algun ide que soporte python como IntelliJ por ejemplo, un entorno donde se probo y funciono.

o alternativamente, correr utilizando la consola de comandos y el commando:

    c:\...\{ruta archivo}>python {nombre archivo}.py

</p>
</details>

- - -

## Sobre el proyecto

Comenzaremos explicando el código del servidor, en primer lugar se importa la librería socket de python luego creamos un socket con la línea socket.socket(socket.AF_INET, socket.SOCK_STREAM) la cual nos permite crear un socket TCP.

```
import socket

sServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Una vez creado el socket, establecemos la dirección que utilizará el servidor (direccion_server) y lo inicializamos con ella (sServidor.bind(direccion_server))

```
direccion_server = ('localhost', 8000)
print('Comenzando en {} puerto {}'.format(*direccion_server))
sServidor.bind(direccion_server)
```

Con el servidor listo, solo falta establecer el número máximo de escuchas que puede soportar así como también la cola de espera, eso se realiza únicamente con la llamada a la función indicada más abajo e identificando el máximo de escuchas.

```
sServidor.listen(5)
```

Para que se acepten las conexiones, el servidor queda escuchando infinitamente hasta que llegue un cliente, para ello se utiliza el primer ciclo while, cuando llega el cliente, el servidor establece la conexión utilizando la llamada .accept(), con dicha llamada guardamos los datos del cliente y su dirección.

```
while True:
    print('Esperando una conexion...')
    cliente, direccion = sServidor.accept()
    print('Conexion establecida con: ', direccion)
```

Una vez aceptada la coneccion con el cliente, se entra en el segundo ciclo while donde se mantiene la coneccion con el cliente hasta que este escriba la palabra “desconectar”, mientras no se envie dicho mensaje, el servidor atenderá indefinidamente al mismo cliente.

```
 while True:
        mensaje = cliente.recv(1024).decode()
        print('Recibido: ', mensaje)

        if mensaje == "desconectar": 
            print("Desconectando cliente")
            break
        cliente.sendall(mensaje.encode()) 

```

Una vez finalizada la comunicación, el servidor termina la comunicación con el cliente y procede a esperar a clientes nuevos o atiende a los que están en la cola de espera. Para finalizar la comunicación utiliza la llamada .close()
```
cliente.close()
print("Conexión cerrada con el cliente")
```

Ahora procederemos a explicar el funcionamiento del cliente, al igual que el servidor, importamos la librería socket, y creamos el socket de la misma forma que el servidor. Además, se establece la dirección del servidor al cual tendrá que conectarse el cliente.

```
import socket
sCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

direccion_server = ('localhost', 8000)
print('Conectando a {} puerto {}'.format(*direccion_server))
sCliente.connect(direccion_server)
```

En nuestro código creamos la variable mensaje y la inicializamos con algo (en este caso un mensaje en blanco) ya que nuestro ciclo while usa como condición el mensaje.

```
mensaje = " "
```

Siguiendo con lo anterior, el cliente entra en un bucle infinito hasta que esté envía el mensaje “desconectar”. Adicionalmente, si el mensaje escrito por el cliente supera los 200 caracteres.

```
while mensaje != 'desconectar':
mensaje = input('Escriba el mensaje a enviar: ')
if len(mensaje) > 200:
print('l mensaje no puede superar los 200 caracteres.')
continue
sCliente.sendall(mensaje.encode())
recibo = sCliente.recv(1024).decode()
print('Mensaje recibido: ', recibo)
```

Cuando el cliente envía el mensaje “desconectar” el mensaje es enviado y se sale del ciclo while, finalmente, el socket es cerrado mediante la llamada a .close()

```
print('Cerrando Socket')
sCliente.close()
```

Cabe destacar que el código fuente de ambos códigos (Cliente y Servidor) se encuentran comentados. Los comentarios fueron quitados únicamente para una mejor legibilidad en el informe

- - -
