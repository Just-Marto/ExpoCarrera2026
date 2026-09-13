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
PASOS = {
    1: {
        "titulo": "El código oculto",
        "descripcion": "Esta página esconde algo que no se ve a simple vista. Los desarrolladores a veces dejan cosas en el código fuente...",
        "respuesta": "algoritmo",
        "pistas": [
            "¿Sabías que podés ver el código fuente de cualquier página web? Probá con F12 o Ctrl+U.",
            "Buscá comentarios HTML: son líneas que empiezan con &lt;!-- y terminan con --&gt;",
            "El comentario dice: la clave es \"algoritmo\"",
        ],
    },
    2: {
        "titulo": "El mensaje cifrado",
        "descripcion": "Encontraste un mensaje, pero está codificado. Los datos en internet muchas veces viajan disfrazados...",
        "respuesta": "robots.txt",
        "pistas": [
            "El texto extraño es Base64, una codificación muy usada en la web. Buscá \"decodificar base64 online\".",
            "Copiá el texto y pegalo en base64decode.org",
            "El texto decodificado dice: robots.txt",
        ],
    },
    3: {
        "titulo": "El archivo secreto",
        "descripcion": "Sabés que existe un archivo oculto en el servidor. ¿Podés encontrarlo?",
        "respuesta": "cortafuegos",
        "pistas": [
            "robots.txt es un archivo que los sitios web usan para dar instrucciones a buscadores. Probá acceder a /ctf/robots.txt",
            "Abrí el navegador y andá a: http://localhost:5000/ctf/robots.txt",
            "El archivo contiene la palabra: cortafuegos",
        ],
    },
    4: {
        "titulo": "La flag final",
        "descripcion": "Ya tenés todas las piezas. En ciberseguridad, las respuestas se entregan como \"flags\" con un formato especial.",
        "respuesta": "CTF{cortafuegos}",
        "pistas": [
            "El formato de flag es: CTF{palabra}",
            "¿Cuál fue la última palabra que encontraste?",
            "La flag es: CTF{cortafuegos}",
        ],
    },
}


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
    session.pop("ctf_completados", None)
    return redirect(url_for("ctf.dashboard"))


@ctf_bp.route("/paso/<int:num>")
def paso(num):
    if num not in PASOS:
        return redirect(url_for("ctf.dashboard"))
    if not paso_desbloqueado(num):
        return redirect(url_for("ctf.dashboard"))

    completados = get_progreso()
    return render_template(
        f"ctf_paso{num}.html",
        paso=PASOS[num],
        num=num,
        completados=completados,
        total=len(PASOS),
        desbloqueado=True,
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

        return render_template(
            f"ctf_paso{num}.html",
            paso=PASOS[num],
            num=num,
            completados=completados,
            total=len(PASOS),
            exito=True,
            siguiente=num + 1 if num < len(PASOS) else None,
        )
    else:
        return render_template(
            f"ctf_paso{num}.html",
            paso=PASOS[num],
            num=num,
            completados=completados,
            total=len(PASOS),
            error="Respuesta incorrecta. ¡Seguí intentando!",
        )


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


# ── Archivo oculto para el paso 3 ──
@ctf_bp.route("/robots.txt")
def robots():
    return (
        "# CyberQuest - Archivo de configuración\n"
        "# Los robots de búsqueda no deberían indexar esto...\n"
        "#\n"
        "# Pero si llegaste hasta acá, ¡bien hecho!\n"
        "# CLAVE-PASO-3: cortafuegos\n"
        "#\n"
        "User-agent: *\n"
        "Disallow: /ctf/secreto/\n"
    ), 200, {"Content-Type": "text/plain; charset=utf-8"}
