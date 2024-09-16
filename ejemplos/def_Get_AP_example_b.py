# Importar la clase TPicoESPC3
from TPicoESPC3 import ESPC3
import time

# Configuración de las credenciales Wi-Fi
secrets = {
    "ssid": "TELWINET:9E-5E_EXT",
    "password": "68297640"
}

# Inicializar el módulo ESP32C3
esp = ESPC3()

# Intentar conectar a la red Wi-Fi
try:
    esp.connect(secrets)
    print("Conectado a la red Wi-Fi:", secrets["ssid"])
except Exception as e:
    print("Error al conectar:", e)

# Obtener la lista de puntos de acceso
try:
    ap_list = esp.get_AP()
    print("Puntos de acceso disponibles:")
    labels = ["Seguridad", "SSID", "RSSI", "MAC", "Canal", 
              "Tipo de escaneo", "Tiempo mínimo de escaneo", 
              "Tiempo máximo de escaneo", "Par de cifrado", 
              "Grupo de cifrado", "Soporte 802.11", "WPS"]
    
    for ap in ap_list:
        for i, label in enumerate(labels):
            print(f"{label}:\n{ap[i]}\n")
except Exception as e:
    print("Error al obtener puntos de acceso:", e)
