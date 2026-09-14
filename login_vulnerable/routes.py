"""
Rutas del módulo de login vulnerable.

VULNERABILIDAD INTENCIONAL — solo para demo educativa.

Este login ES el paso 4 (final) de CyberQuest: solo se puede llegar a el
despues de completar los pasos 1-3 del CTF. Entrar exitosamente como admin
(con la credencial debil admin/admin) marca el paso 4 como completado. La
falla de seguridad no es una SQL injection, sino una contrasena debil sin
ningun tipo de proteccion contra fuerza bruta (sin limite de intentos, sin
bloqueo de cuenta).
"""
import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for, session
from login_vulnerable.db import DB_PATH
from ctf.routes import PASO_LOGIN, paso_desbloqueado, get_progreso

login_bp = Blueprint(
    "login",
    __name__,
    template_folder="templates",
)

# Wordlist de ejemplo que "prueba" el atacante — la misma que anima el boton
# de fuerza bruta en login.html. La ultima siempre es la contrasena real.
INTENTOS_FUERZA_BRUTA = ["1234", "qwerty", "123456", "admin"]

MAX_INTENTOS_SEGURO = 3


def login_desbloqueado():
    """El login (paso 4) solo se desbloquea tras completar los pasos 1-3."""
    return paso_desbloqueado(PASO_LOGIN)


def marcar_paso4_completado():
    completados = get_progreso()
    completados.add(PASO_LOGIN)
    session["ctf_completados"] = list(completados)


# ── Versión VULNERABLE (contraseña débil, sin límite de intentos) ──

@login_bp.route("/login")
def login_page():
    if not login_desbloqueado():
        return redirect(url_for("ctf.dashboard"))
    return render_template("login.html", intentos_wordlist=INTENTOS_FUERZA_BRUTA)


@login_bp.route("/login", methods=["POST"])
def login_submit():
    if not login_desbloqueado():
        return redirect(url_for("ctf.dashboard"))

    username = request.form.get("username", "")
    password = request.form.get("password", "")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM usuarios WHERE username = ? AND password = ?",
        (username, password),
    )
    user = cursor.fetchone()
    conn.close()

    if user and username == "admin" and password == "admin":
        # Credencial debil adivinada por fuerza bruta: paso 4 completado.
        marcar_paso4_completado()
        return render_template(
            "hacked.html",
            username=user[1],
            intentos=INTENTOS_FUERZA_BRUTA,
        )
    elif user:
        return render_template("dashboard.html", username=user[1])
    else:
        return render_template(
            "login.html",
            error="Usuario o contraseña incorrectos",
            username=username,
            intentos_wordlist=INTENTOS_FUERZA_BRUTA,
        )


# ── Versión SEGURA (para comparar) ──

@login_bp.route("/login-seguro")
def login_seguro_page():
    if not login_desbloqueado():
        return redirect(url_for("ctf.dashboard"))
    intentos_fallidos = session.get("intentos_fallidos_seguro", 0)
    return render_template(
        "login_seguro.html",
        bloqueado=intentos_fallidos >= MAX_INTENTOS_SEGURO,
    )


@login_bp.route("/login-seguro", methods=["POST"])
def login_seguro_submit():
    if not login_desbloqueado():
        return redirect(url_for("ctf.dashboard"))

    intentos_fallidos = session.get("intentos_fallidos_seguro", 0)

    # ✅ SEGURA: limite de intentos + bloqueo de cuenta.
    # Asi se previene la fuerza bruta: ya no importa que tan buena sea la
    # wordlist del atacante, el sistema corta despues de N intentos fallidos.
    if intentos_fallidos >= MAX_INTENTOS_SEGURO:
        return render_template(
            "login_seguro.html",
            error="Cuenta bloqueada temporalmente por multiples intentos fallidos. Asi se previene la fuerza bruta.",
            bloqueado=True,
        )

    username = request.form.get("username", "")
    password = request.form.get("password", "")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM usuarios WHERE username = ? AND password = ?",
        (username, password),
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        session["intentos_fallidos_seguro"] = 0
        return render_template("dashboard.html", username=user[1])
    else:
        intentos_fallidos += 1
        session["intentos_fallidos_seguro"] = intentos_fallidos
        restantes = MAX_INTENTOS_SEGURO - intentos_fallidos
        if restantes <= 0:
            return render_template(
                "login_seguro.html",
                error="Cuenta bloqueada temporalmente por multiples intentos fallidos. Asi se previene la fuerza bruta.",
                bloqueado=True,
            )
        return render_template(
            "login_seguro.html",
            error=f"Usuario o contraseña incorrectos. Intentos restantes: {restantes}",
            bloqueado=False,
        )
