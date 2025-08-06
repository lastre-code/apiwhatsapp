import requests
import json

#Token y phone_number_id 
#se debe generar el token y reemplazar este
token = 'EAFbQsRZCagjEBPKYMzZCFmPn4z39o8kMzeezZAyW4lU8JbIf4ZCE0IqKZCqnk9VYimLPSZBlZCVgt1hZBkux7cLW0brC41s9igTZBdcHANMOFM9gyUZCTlbXCpkf4pLAXpZBY7ZA4qy1FqmY0vfB0ZCrCBUmGSDWCDZBQWNs9Ag9UourqUXCEhZA0bZCEzzy0f0ZAlICmEHAfhd3ksmGmZCTIURVSTPtDpZC8HuFLbnswXX0hE8o1bABUozvIoJBVJSr8XTzCK5RZCwZD'
phone_number_id = '755....'  #Este es el que está debajo del numero de prueba, dice identificador del numero de telefono

#URL de la API
url = f'https://graph.facebook.com/v22.0/{phone_number_id}/messages'

#Cabeceras
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

#Cuerpo del mensaje: usando plantilla `hello_world`
payload = {
    'messaging_product': 'whatsapp',
    'to': '57315....', #reemplaza el numero destinatario
    'type': 'template',
    'template': {
        'name': 'hello_world',
        'language': {
            'code': 'en_US'
        }
    }
}

#Envío del mensaje
response = requests.post(url, headers=headers, json=payload)

# Mostrar respuesta
print("Código de respuesta:", response.status_code)
print("Respuesta JSON:", response.json())
