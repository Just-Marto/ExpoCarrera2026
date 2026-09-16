"""
Punto de entrada principal para la expo de ciberseguridad.
Levanta Flask con los módulos de login y CTF en localhost:5000.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.secret_key = "expo-ciberseguridad-2026-demo"

    from login_vulnerable.db import init_db
    from login_vulnerable.routes import login_bp
    from ctf.routes import ctf_bp

    init_db()
    app.register_blueprint(login_bp)
    app.register_blueprint(ctf_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=False, host="127.0.0.1", port=5000)
