import pandas as pd

archivo_csv_entrada = 'NPS_SUZUVAL.csv'
archivo_csv_salida = 'NPS_SUZUVAL_CLEAN.csv'

# Lista de nombres de columnas que deseas conservar
columnas_deseadas = ['Cliente_Id', 
                     'Nota', 
                     'Tipo_Encuesta', 
                     'Punto_Contacto', 
                     'Fecha_Experiencia', 
                     'Fecha_Encuesta', 
                     'Descripcion_Tipo_Encuesta', 
                     'Persona_Nombre', 
                     'Persona_Apellido', 
                     'Contacto_Telefono1', 
                     'Contacto_Email', 
                     'Vendedor_Nombre', 
                     'Asesor_Nombre', 
                     'Marca_Automotriz', 
                     'Modelo_Automotriz_Servicios_Maquinaria',
                     'Verbatim']

# Leer el archivo CSV en un DataFrame de pandas
df = pd.read_csv(archivo_csv_entrada)

# Ordenar por valores en la columna 'edad' de forma ascendente
df = df.sort_values(by=['Nota', 'Tipo_Encuesta'])

# Seleccionar solo las columnas deseadas y guardar en un nuevo archivo CSV
df[columnas_deseadas].to_csv(archivo_csv_salida, index=False)

