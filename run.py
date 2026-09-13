"""
Punto de entrada principal para la expo de ciberseguridad.
Levanta el servidor Flask con ambos módulos (login + CTF).
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Expo Ciberseguridad 2026</h1><p>Servidor funcionando.</p>"

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
