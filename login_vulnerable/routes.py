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
    query = f"SELECT * FROM usuarios WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    # Verificar si las mismas credenciales funcionan con consulta SEGURA.
    # Si la vulnerable encuentra usuario pero la segura no, fue injection.
    cursor.execute(
        "SELECT * FROM usuarios WHERE username = ? AND password = ?",
        (username, password),
    )
    user_safe = cursor.fetchone()
    conn.close()

    if user and not user_safe:
        # Injection detectada: mostrar pantalla educativa
        return render_template(
            "hacked.html",
            username=user[1],
            payload_user=username,
            payload_pass=password,
            query=query,
        )
    elif user:
        # Login legítimo con credenciales correctas
        return render_template("dashboard.html", username=user[1])
    else:
        return render_template("login.html", error="Usuario o contraseña incorrectos")


# ── Versión SEGURA (para comparar) ──

@login_bp.route("/login-seguro")
def login_seguro_page():
    return render_template("login_seguro.html")


@login_bp.route("/login-seguro", methods=["POST"])
def login_seguro_submit():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # ✅ SEGURA: consulta parametrizada. Los ? son placeholders.
    # SQLite recibe datos y comandos por separado = imposible inyectar SQL.
    cursor.execute(
        "SELECT * FROM usuarios WHERE username = ? AND password = ?",
        (username, password),
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        return render_template("dashboard.html", username=user[1])
    else:
        return render_template(
            "login_seguro.html",
            error="Usuario o contraseña incorrectos — la inyección no funciona acá.",
        )
