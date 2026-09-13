# Expo Ciberseguridad — Ingeniería en Sistemas 2026

> **⚠️ ADVERTENCIA:** Este proyecto contiene código **intencionalmente vulnerable** con fines educativos. NO usar en producción ni exponer a redes públicas.

## ¿Qué es?

Estación interactiva para una expo universitaria que demuestra conceptos de ciberseguridad de forma práctica:

1. **Login Vulnerable (SQL Injection)** — Un campus virtual ficticio ("UniDemo") con una vulnerabilidad real de SQL injection. El visitante intenta "hackear" el login, ve una explicación paso a paso de qué pasó y por qué, y luego compara con la versión segura.

2. **Mini-CTF** — Desafío de 4 pasos encadenados (pistas en código fuente, Base64, archivos ocultos) que el visitante resuelve en ~5 minutos.

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
| `http://localhost:5000/login` | Login vulnerable (demo principal) |
| `http://localhost:5000/login-seguro` | Login seguro (para comparar) |

### Credenciales de prueba

| Usuario | Contraseña |
|---------|------------|
| admin | admin123 |
| maria | clave456 |
| juan | segura789 |

### Payload de SQL injection

Escribir en cualquiera de los campos del login vulnerable:
```
' OR '1'='1
```

## Stack

- Python 3 + Flask
- SQLite
- HTML / CSS / JS (sin frameworks)

## Estructura

```
├── login_vulnerable/        # Módulo 1: Demo SQL injection
│   ├── db.py               # Base de datos SQLite con usuarios
│   ├── routes.py           # Rutas Flask (vulnerable + segura)
│   └── templates/          # HTMLs del login
├── ctf/                     # Módulo 2: Mini-CTF de 4 pasos
├── static/css/              # Estilos
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
