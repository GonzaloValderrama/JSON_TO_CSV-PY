import pandas as pd

archivo_csv_entrada = 'NPS_SUZUVAL.csv'
archivo_csv_VENTAS = 'C:\\SUZUVAL\\FINAL_NPS_SUZUVAL\\NPS_VENTAS_09-2023.csv'
archivo_csv_SSTT = 'C:\\SUZUVAL\\FINAL_NPS_SUZUVAL\\NPS_SSTT_09-2023.csv'

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

# Seleccionar filas donde la columna 'Tipo_Encuesta' contiene el texto 'Servicio Técnico'
df_SSTT = df[df['Tipo_Encuesta'].str.contains('Servicio Técnico')]

# Ordenar por valores en la columna 'Nota' de forma ascendente
df_SSTT = df_SSTT.sort_values(by='Nota')

# Seleccionar solo las columnas deseadas y guardar en un nuevo archivo CSV
df_SSTT[columnas_deseadas].to_csv(archivo_csv_SSTT, index=False)

# Seleccionar filas donde la columna 'Tipo_Encuesta' contiene el texto 'Venta Nuevos'
df_VENTAS = df[df['Tipo_Encuesta'].str.contains('Venta Nuevos')]

# Ordenar por valores en la columna 'Nota' de forma ascendente
df_VENTAS = df_VENTAS.sort_values(by='Nota')

# Seleccionar solo las columnas deseadas y guardar en un nuevo archivo CSV
df_VENTAS[columnas_deseadas].to_csv(archivo_csv_VENTAS, index=False)