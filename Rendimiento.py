import psutil
import speedtest
from pygetwindow import getWindowsWithTitle

def obtener_rendimiento_cpu():
    return psutil.cpu_percent(interval=1)

def obtener_rendimiento_memoria():
    return psutil.virtual_memory().percent

def obtener_temperatura_cpu():
    try:
        # Buscar la ventana de OpenHardwareMonitor
        ventana_ohm = getWindowsWithTitle('Open Hardware Monitor')[0]
        
        # Extraer el texto de la ventana que contiene la información de temperatura
        texto_ventana = ventana_ohm.text
        inicio_temperatura = texto_ventana.find('Temperature')
        fin_temperatura = texto_ventana.find('°C', inicio_temperatura)
        temperatura = float(texto_ventana[inicio_temperatura + 12:fin_temperatura])
        
        return temperatura
    except Exception as e:
        print(f"No se pudo obtener la temperatura del CPU: {e}")
        return None

def obtener_rendimiento_red():
    st = speedtest.Speedtest()
    velocidad_subida = st.upload() / 1024 / 1024  # Convertir a Mbps
    velocidad_bajada = st.download() / 1024 / 1024  # Convertir a Mbps
    return velocidad_subida, velocidad_bajada

# Mostrar resultados
print(f"Rendimiento CPU: {obtener_rendimiento_cpu()}%")
print(f"Rendimiento Memoria: {obtener_rendimiento_memoria()}%")
temperatura = obtener_temperatura_cpu()
print(f"Temperatura CPU: {temperatura}°C" if temperatura is not None else "No se pudo obtener la temperatura del CPU.")
velocidad_subida, velocidad_bajada = obtener_rendimiento_red()
print(f"Velocidad de Subida: {velocidad_subida:.2f} Mbps")
print(f"Velocidad de Bajada: {velocidad_bajada:.2f} Mbps")
