# Importar los módulos necesarios
import psutil
import socket

# Definir las funciones para obtener el rendimiento de la PC local
def obtener_rendimiento_cpu_local():
    return psutil.cpu_percent(interval=1)

def obtener_rendimiento_memoria_local():
    return psutil.virtual_memory().percent

def obtener_rendimiento_red_local():
    return psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv

def obtener_temperatura_cpu_local():
    return psutil.sensors_temperatures()['coretemp'][0].current

# Definir la función para obtener el rendimiento de la PC remota
def obtener_rendimiento_remoto():
    # Enviar un mensaje al servidor
    mensaje = "Hola, soy el cliente"
    objetoSocket.sendall(mensaje.encode())

    # Recibir la respuesta del servidor
    respuesta = objetoSocket.recv(1024)
    print("El servidor dice:", respuesta.decode())

    # Extraer los datos de rendimiento de la respuesta
    datos = respuesta.decode().split(",")
    rendimiento_cpu = float(datos[0])
    rendimiento_memoria = float(datos[1])
    rendimiento_red = (float(datos[2]), float(datos[3]))
    temperatura_cpu = float(datos[4])
    
    return rendimiento_cpu, rendimiento_memoria, rendimiento_red, temperatura_cpu

# Crear un objeto socket TCP/IP
objetoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto del servidor
servidor = "10.3.21.188" # La dirección IP de la otra PC
puerto = 8000 # El puerto de conexión
objetoSocket.connect((servidor, puerto))

# Mostrar los resultados del rendimiento de la PC local
print(f"Rendimiento CPU Local: {obtener_rendimiento_cpu_local()}%")
print(f"Rendimiento Memoria Local: {obtener_rendimiento_memoria_local()}%")
print(f"Rendimiento Red Local: {obtener_rendimiento_red_local()}")
print(f"Temperatura CPU Local: {obtener_temperatura_cpu_local()}°C")

# Mostrar los resultados del rendimiento de la PC remota
rendimiento_cpu, rendimiento_memoria, rendimiento_red, temperatura_cpu = obtener_rendimiento_remoto()
print(f"Rendimiento CPU Remoto: {rendimiento_cpu}%")
print(f"Rendimiento Memoria Remoto: {rendimiento_memoria}%")
print(f"Rendimiento Red Remoto: {rendimiento_red}")
print(f"Temperatura CPU Remoto: {temperatura_cpu}°C")

# Cerrar el socket
objetoSocket.close()