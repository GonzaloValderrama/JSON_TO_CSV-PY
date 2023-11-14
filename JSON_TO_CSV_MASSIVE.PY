import os
import pandas as pd

# Ruta del directorio que contiene los archivos JSON
directorio_json = r'C:\GONZALO\NPS\Encuestas'
# Ruta del directorio donde se guardarán los archivos CSV
directorio_csv = r'C:\GONZALO\NPS\Encuestas'

# Crear el directorio CSV si no existe
if not os.path.exists(directorio_csv):
    os.makedirs(directorio_csv)

# Lista para almacenar todos los DataFrames
dataframes = []

# Iterar sobre cada archivo en el directorio JSON
for archivo_json in os.listdir(directorio_json):
    if archivo_json.endswith('.json'):
        # Crear la ruta completa del archivo
        ruta_json = os.path.join(directorio_json, archivo_json)

        # Leer el archivo JSON y almacenar el DataFrame en la lista
        df_json = pd.read_json(ruta_json)
        dataframes.append(df_json)

# Concatenar todos los DataFrames en uno solo
df_final = pd.concat(dataframes, ignore_index=True)

# Guardar el DataFrame combinado en un nuevo archivo CSV
archivo_salida = os.path.join(directorio_csv, 'compilado_encuestas_nps.csv')
df_final.to_csv(archivo_salida, index=False)

print(f"Archivos JSON combinados y guardados en {archivo_salida}.")
