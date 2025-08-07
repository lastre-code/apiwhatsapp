from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "iconicKey"  # Token de verificación personalizado

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Validación del webhook
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("✅ Webhook verificado correctamente")
            return challenge, 200
        else:
            print("❌ Falló la verificación del webhook")
            return "Error de verificación", 403

    elif request.method == "POST":
        # Manejo de eventos entrantes de WhatsApp
        data = request.get_json()
        print("📩 Evento recibido:")
        print(data)
        return "Evento recibido", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
