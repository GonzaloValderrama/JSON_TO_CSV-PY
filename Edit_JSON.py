import os
import json

def eliminar_primeros_y_ultimo_caracter(archivo_entrada, archivo_salida):
    # Abrir el archivo de entrada y leer su contenido
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Eliminar los primeros 36 caracteres y el último caracter
    nuevo_contenido = contenido[37:-1]

    # Escribir el nuevo contenido en el archivo de salida
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(nuevo_contenido)

def procesar_archivos_json(directorio_entrada, directorio_salida):
    # Asegurarse de que el directorio de salida exista
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    # Obtener la lista de archivos JSON en el directorio de entrada
    archivos_json = [archivo for archivo in os.listdir(directorio_entrada) if archivo.endswith('.json')]

    # Procesar cada archivo JSON
    for archivo in archivos_json:
        ruta_entrada = os.path.join(directorio_entrada, archivo)
        ruta_salida = os.path.join(directorio_salida, archivo)
        eliminar_primeros_y_ultimo_caracter(ruta_entrada, ruta_salida)

# Directorio que contiene los archivos JSON originales
directorio_entrada = r'C:\SUZUVAL\Lineage\Encuestas_NPS_Json_2023\Dota'
# Directorio de salida para los archivos procesados
directorio_salida = r'C:\SUZUVAL\Lineage\Encuestas_NPS_Json_2023\Dota\JSON_modificados'

# Llamar a la función para procesar los archivos JSON
procesar_archivos_json(directorio_entrada, directorio_salida)


