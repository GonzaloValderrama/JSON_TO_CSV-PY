
import pandas as pd

# Carga el archivo JSON
df = pd.read_json("Septiembre.json")

# Escribe el DataFrame en un archivo CSV
df.to_csv("NPS_SUZUVAL.csv")

