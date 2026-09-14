# Expo Ciberseguridad — Ingeniería en Sistemas 2026

> **⚠️ ADVERTENCIA:** Este proyecto contiene código **intencionalmente vulnerable** con fines educativos. NO usar en producción ni exponer a redes públicas.

## ¿Qué es?

Estación interactiva para una expo universitaria que demuestra conceptos de ciberseguridad de forma práctica:

**Mini-CTF (CyberQuest)** — Desafío de 4 pasos encadenados que el visitante resuelve en ~5 minutos: pistas en código fuente, Base64 y archivos ocultos (pasos 1-3), y como cierre (paso 4) el login real de un campus virtual ficticio ("UniDemo") con un login sin límite de intentos y una contraseña débil. El visitante simula un ataque de fuerza bruta contra el usuario `admin`, ve una explicación paso a paso de qué pasó y por qué, y luego compara con la versión segura (con bloqueo de cuenta).

## Inicio rápido (un solo comando)

**Windows — doble click en `iniciar.bat`** o desde terminal:

```bash
iniciar.bat
```

Esto crea el entorno virtual, instala dependencias, y arranca el servidor. Abrir `http://localhost:5000` en el navegador.

Para parar: `Ctrl+C` en la terminal.

### Inicio manual (si preferís)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## URLs del proyecto

| URL | Descripción |
|-----|-------------|
| `http://localhost:5000/` | Página de inicio |
| `http://localhost:5000/ctf/` | CyberQuest — CTF de 4 pasos (empieza acá) |
| `http://localhost:5000/login` | Login vulnerable — paso 4 del CTF (se desbloquea al completar pasos 1-3) |
| `http://localhost:5000/login-seguro` | Login seguro (para comparar) |
| `http://localhost:5000/ctf/completado` | Pantalla de victoria — se llega ahí al entrar al login como admin |

### Material imprimible

| Archivo | Descripción |
|---------|-------------|
| `static/imprimibles/cartel-desafio.html` | Cartel A4 apaisado para la mesa del login |
| `static/imprimibles/hoja-mision.html` | Hoja de misión A4 para visitantes del CTF |
| `static/imprimibles/ranking.html` | Tabla de ranking A4 para anotar tiempos |

Abrir en el navegador e imprimir con Ctrl+P.

### Credenciales de prueba

| Usuario | Contraseña |
|---------|------------|
| admin | admin |
| maria | clave456 |
| juan | segura789 |

### Ataque de fuerza bruta

El login vulnerable (paso 4 del CTF, tras completar los pasos 1-3) no tiene límite de intentos. El usuario `admin` tiene una contraseña débil (`admin`). El botón "Simular ataque de fuerza bruta" en la página de login anima una wordlist de prueba (`1234`, `qwerty`, `123456`, `admin`) contra ese usuario hasta encontrarla.

## Stack

- Python 3 + Flask
- SQLite
- HTML / CSS / JS (sin frameworks)

## Estructura

```
├── ctf/                     # Módulo 1: Mini-CTF de 4 pasos (empieza acá)
│   ├── routes.py           # Rutas Flask del CTF
│   └── templates/          # HTMLs de cada paso + dashboard
├── login_vulnerable/        # Módulo 2: Demo de fuerza bruta (desafío final)
│   ├── db.py               # Base de datos SQLite con usuarios
│   ├── routes.py           # Rutas Flask (vulnerable + segura)
│   └── templates/          # HTMLs del login
├── templates/home.html      # Página de inicio
├── static/css/              # Estilos (login, ctf, home)
├── static/imprimibles/      # Cartel, hoja de misión, ranking (A4)
├── SOLUCIONES.md            # Respuestas del CTF (solo presentador)
├── iniciar.bat              # Arranque con un solo comando (Windows)
├── run.py                   # Punto de entrada Flask
├── requirements.txt         # Dependencias (Flask)
└── README.md
```

## Mensaje central

El objetivo NO es mostrar "qué fácil es atacar", sino demostrar **cómo se previenen** estas vulnerabilidades. Cada demo incluye la explicación de la defensa.

## Autor

Proyecto educativo para Expo Ingeniería en Sistemas 2026.

## Licencia

Uso educativo únicamente.
