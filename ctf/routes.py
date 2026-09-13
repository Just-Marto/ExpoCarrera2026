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
        "descripcion": "Interceptaste un mensaje codificado. Usa el decodificador integrado para descifrar que dice.",
        "respuesta": "configuracion",
        "pistas": [
            "El texto esta codificado en Base64, un formato muy usado en la web. Copia el texto y pegalo en el decodificador de abajo.",
            "El simbolo <code>=</code> al final es tipico de Base64. Proba decodificarlo y fijate que palabra aparece.",
            "La respuesta es: <strong>configuracion</strong>",
        ],
    },
    3: {
        "titulo": "El archivo secreto",
        "descripcion": "Sabes que existe un archivo de configuracion oculto en el servidor. ¿Podes encontrarlo?",
        "respuesta": "cortafuegos",
        "pistas": [
            "El paso anterior te dio una palabra clave... ¿que pasa si intentas acceder a ese archivo en el navegador?",
            "Proba navegar a: <code>localhost:5000/ctf/configuracion</code>",
            "La respuesta es: <strong>cortafuegos</strong>",
        ],
    },
    4: {
        "titulo": "La flag final",
        "descripcion": "El sistema tiene una contrasena hardcodeada en el codigo fuente de esta pagina. Los desarrolladores a veces dejan credenciales expuestas. Encontrala.",
        "respuesta": "CTF{seguridad_total}",
        "pistas": [
            "¿Recordas como encontraste la respuesta del paso 1? Esta pagina tambien esconde algo en su codigo fuente...",
            "Abri el codigo fuente de ESTA pagina (Ctrl+U) y busca un comentario o variable con la flag.",
            "La respuesta es: <strong>CTF{seguridad_total}</strong>",
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
            error="Respuesta incorrecta. ¡Segui intentando!",
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


# ── Archivo de configuración oculto para el paso 3 ──
@ctf_bp.route("/configuracion")
def configuracion():
    return render_template("ctf_config.html")
