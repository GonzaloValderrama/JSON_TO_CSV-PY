import requests
import json

# URL para obtener respuesta de la API
url = "https://ipa.prd.derco.services/administracion-nps/v1/respuesta/ces"

#Completar datos para codigo CES, periodo fecha y token.
params = {
    "codigo": "C006",
    "periodo": "2023-09",
    "token": "223e13def1747dcf08697118349cea6525a374c0aa957b34a5c9bd874da790c4"
}

headers = {
    "x-apikey": "6sxtF8nGtZY8tGcIqKg1IGuP3oHH5jyRAA5ZYPel8vWRGG4g",
    }

# Realizar la solicitud GET con parámetros y encabezados
response = requests.get(url, params=params, headers=headers)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # La solicitud fue exitosa
    json_data = response.json()
    # Guardar la respuesta en un archivo JSON
    with open(r"C:\SUZUVAL\NPS\Solicitud_JSON\NPS_2023_09.json", "w") as json_file:
        json.dump(json_data, json_file)
    print("Respuesta guardada en 'NPS_2023_09.json'")
else:
    # La solicitud falló, imprimir el código de estado y el mensaje de error
    print(f"Error {response.status_code}: {response.text}")
