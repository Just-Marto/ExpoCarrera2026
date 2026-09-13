"""
Rutas del módulo de login vulnerable.

Por ahora: validación CORRECTA con consultas parametrizadas.
En el Paso 1b vamos a introducir la vulnerabilidad.
"""
import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for
from login_vulnerable.db import DB_PATH

login_bp = Blueprint(
    "login",
    __name__,
    template_folder="templates",
)


@login_bp.route("/")
def index():
    return redirect(url_for("login.login_page"))


@login_bp.route("/login")
def login_page():
    return render_template("login.html")


@login_bp.route("/login", methods=["POST"])
def login_submit():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Consulta parametrizada — SEGURA.
    # Los signos ? son placeholders: SQLite inserta los valores
    # de forma segura, sin mezclarlos con el SQL.
    cursor.execute(
        "SELECT * FROM usuarios WHERE username = ? AND password = ?",
        (username, password),
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        return render_template("dashboard.html", username=user[1])
    else:
        return render_template("login.html", error="Usuario o contraseña incorrectos")
