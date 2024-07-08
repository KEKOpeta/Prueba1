import requests

# URL del webhook de Discord
webhook_url = 'https://discord.com/api/webhooks/1259953420589334579/kKHuAUWmW7DIeDOToMF6DxJMJ9PsMQ_21rEaP-s6dhDe0eCc3tNVC9JQ7eoQpDDgxKqp'

# Contenido del mensaje
message = {
    "content": "Besitos pa tu clito"
}

# Enviar la solicitud POST al webhook de Discord
response = requests.post(webhook_url, json=message)

if response.status_code == 204:
    print("Mensaje enviado con éxito")
else:
    print(f"Error al enviar el mensaje: {response.status_code}")
