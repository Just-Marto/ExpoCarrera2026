# Expo Ciberseguridad — Ingeniería en Sistemas 2026

> **⚠️ ADVERTENCIA:** Este proyecto contiene código **intencionalmente vulnerable** con fines educativos. NO usar en producción ni exponer a redes públicas.

## ¿Qué es?

Estación interactiva para una expo universitaria que demuestra conceptos de ciberseguridad de forma práctica:

1. **Login Vulnerable** — Un formulario de login con una vulnerabilidad real de SQL injection. El visitante intenta "hackear" el login, y luego ve la explicación de cómo se previene.

2. **Mini-CTF** — Desafío de 4 pasos encadenados (pistas en código fuente, Base64, archivos ocultos) que el visitante resuelve en ~5 minutos.

## Stack

- Python 3 + Flask
- SQLite
- HTML / CSS / JS (sin frameworks)

## Cómo correr

```bash
# Crear entorno virtual e instalar dependencias
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt

# Iniciar la aplicación
python run.py
```

Abrir `http://localhost:5000` en el navegador.

## Estructura

```
├── login-vulnerable/    # Módulo 1: Demo SQL injection
├── ctf/                 # Módulo 2: Mini-CTF de 4 pasos
├── requirements.txt     # Dependencias Python
├── run.py              # Script de arranque
└── README.md
```

## Mensaje central

El objetivo NO es mostrar "qué fácil es atacar", sino demostrar **cómo se previenen** estas vulnerabilidades. Cada demo incluye la explicación de la defensa.

## Autor

Proyecto educativo para Expo Ingeniería en Sistemas 2026.

## Licencia

Uso educativo únicamente.
