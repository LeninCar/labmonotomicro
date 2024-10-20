from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/cachetada', methods=['GET'])
def get_cachetada():
    # Lógica del servicio cachetadacontrucha
    response = {
        "message": "Hola, soy servicio3 Cachetada con Trucha !",
        "action": "cachetada",
        "power": 100
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
