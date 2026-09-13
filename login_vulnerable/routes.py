"""
Rutas del módulo de login vulnerable.

VULNERABILIDAD INTENCIONAL — solo para demo educativa.
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

    # ⚠️ VULNERABLE: el input del usuario se concatena DIRECTO en el SQL.
    # Esto permite SQL injection porque el motor de la base de datos no puede
    # distinguir qué parte es "comando SQL" y qué parte es "dato del usuario".
    query = f"SELECT * FROM usuarios WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    user = cursor.fetchone()
    conn.close()

    if user:
        return render_template("dashboard.html", username=user[1])
    else:
        return render_template("login.html", error="Usuario o contraseña incorrectos")
