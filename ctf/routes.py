"""
Rutas del mini-CTF "CyberQuest" — 4 pasos encadenados.

Usa Flask sessions para trackear progreso del visitante.
"""
from flask import Blueprint, render_template, request, redirect, url_for, session

ctf_bp = Blueprint(
    "ctf",
    __name__,
    template_folder="templates",
    url_prefix="/ctf",
)

# ── Definición de los 4 pasos ──
# Cada paso tiene: título, descripción, respuesta correcta, y pistas graduadas.
# IMPORTANTE: la pista 3 siempre da la respuesta directa (destraba al visitante).
PASOS = {
    1: {
        "titulo": "El codigo oculto",
        "descripcion": "Esta pagina esconde algo que no se ve a simple vista. Los desarrolladores a veces dejan cosas en el codigo fuente...",
        "respuesta": "algoritmo",
        "pistas": [
            "Los navegadores tienen herramientas para ver lo que hay 'detras' de una pagina web. Proba con F12 o Ctrl+U.",
            "Busca comentarios HTML: son lineas que empiezan con &lt;!-- y terminan con --&gt;. Hay uno cerca del inicio del codigo.",
            "La respuesta es: <strong>algoritmo</strong>",
        ],
    },
    2: {
        "titulo": "El mensaje cifrado",
        "descripcion": "Interceptaste un mensaje codificado. Usa un decodificador Base64 para descifrar que dice.",
        "respuesta": "configuracion",
        "pistas": [
            "El texto esta codificado en Base64, un formato muy usado en la web.",
            "Copia el texto y pegalo en <a href=\"https://www.base64decode.org/es/\" target=\"_blank\" rel=\"noopener noreferrer\">base64decode.org/es</a> (el boton de la pagina te lleva ahi).",
            "La respuesta es: <strong>configuracion</strong>",
        ],
    },
    3: {
        "titulo": "El archivo secreto",
        "descripcion": "Sabes que existe un archivo de configuracion oculto en el servidor. ¿Podes encontrarlo y descubrir que datos sensibles contiene?",
        "respuesta": "cortafuegos",
        "pistas": [
            "El paso anterior te dio una palabra clave... ¿que pasa si intentas acceder a ese archivo en el navegador?",
            "Proba navegar a: <code>{host}/ctf/configuracion</code>",
            "La respuesta es: <strong>cortafuegos</strong>",
        ],
    },
    4: {
        "titulo": "El login vulnerable",
        "descripcion": "El ultimo desafio no esta escondido en el codigo: es el login real del campus virtual UniDemo. El usuario admin tiene una contrasena debil y el sistema no bloquea intentos. Entra sin conocerla.",
        "pistas": [
            "Anda al login del campus y fijate si hay alguna herramienta que te ayude a probar contrasenas automaticamente.",
            "La contrasena de <code>admin</code> es una de las mas usadas del mundo. No hace falta una wordlist gigante.",
            "En el login, usa el boton <strong>Simular ataque de fuerza bruta</strong>: la contrasena es <strong>admin</strong>.",
        ],
    },
}

# El paso 4 no se resuelve con un formulario de texto: se completa entrando
# al login vulnerable (login_vulnerable/routes.py marca este paso al detectar
# el login exitoso con la credencial debil admin/admin).
PASO_LOGIN = 4


def get_progreso():
    """Devuelve set de pasos completados desde la sesión."""
    return set(session.get("ctf_completados", []))


def paso_desbloqueado(num):
    """Un paso está desbloqueado si es el 1 o si el anterior está completado."""
    if num == 1:
        return True
    return (num - 1) in get_progreso()


# ── Rutas ──

@ctf_bp.route("/")
def dashboard():
    completados = get_progreso()
    return render_template(
        "ctf_dashboard.html",
        pasos=PASOS,
        completados=completados,
        total=len(PASOS),
    )


@ctf_bp.route("/reset")
def reset():
    # Limpia todo el progreso: los 4 pasos del CTF (incluido el login,
    # que es el paso 4) y el contador de intentos del login seguro.
    session.pop("ctf_completados", None)
    session.pop("ctf_flash", None)
    session.pop("intentos_fallidos_seguro", None)
    return redirect("/")


@ctf_bp.route("/paso/<int:num>")
def paso(num):
    if num not in PASOS:
        return redirect(url_for("ctf.dashboard"))
    if not paso_desbloqueado(num):
        return redirect(url_for("ctf.dashboard"))

    completados = get_progreso()
    flash = session.pop("ctf_flash", None) or {}
    return render_template(
        f"ctf_paso{num}.html",
        paso=PASOS[num],
        num=num,
        completados=completados,
        total=len(PASOS),
        desbloqueado=True,
        exito=flash.get("exito"),
        siguiente=flash.get("siguiente"),
        error=flash.get("error"),
    )


@ctf_bp.route("/paso/<int:num>/verificar", methods=["POST"])
def verificar(num):
    if num not in PASOS:
        return redirect(url_for("ctf.dashboard"))

    respuesta = request.form.get("respuesta", "").strip()
    correcta = respuesta.lower() == PASOS[num]["respuesta"].lower()

    completados = get_progreso()

    if correcta:
        completados.add(num)
        session["ctf_completados"] = list(completados)

        if len(completados) == len(PASOS):
            return redirect(url_for("ctf.completado"))

        # Redirect (Post/Redirect/Get) para que el navegador no deje el POST
        # en el historial: asi el boton de "volver atras" no pide reenviar
        # el formulario.
        session["ctf_flash"] = {
            "exito": True,
            "siguiente": num + 1 if num < len(PASOS) else None,
        }
        return redirect(url_for("ctf.paso", num=num))
    else:
        session["ctf_flash"] = {"error": "Respuesta incorrecta. ¡Segui intentando!"}
        return redirect(url_for("ctf.paso", num=num))


@ctf_bp.route("/completado")
def completado():
    completados = get_progreso()
    if len(completados) < len(PASOS):
        return redirect(url_for("ctf.dashboard"))
    return render_template(
        "ctf_completado.html",
        total=len(PASOS),
        completados=completados,
    )


# ── Archivo de configuración oculto para el paso 3 ──
@ctf_bp.route("/configuracion")
def configuracion():
    return render_template("ctf_config.html")
