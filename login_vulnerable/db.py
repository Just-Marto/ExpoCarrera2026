"""
Inicializa la base de datos SQLite con usuarios de ejemplo.

Esto crea una tabla 'usuarios' con 3 cuentas de prueba.
La base se regenera cada vez que arranca la app (por eso .db está en .gitignore).
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "usuarios.db")


def init_db():
    """Crea la tabla de usuarios y carga datos de ejemplo."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS usuarios")
    cursor.execute("""
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    usuarios_ejemplo = [
        ("admin", "admin"),
        ("maria", "clave456"),
        ("juan", "segura789"),
    ]
    cursor.executemany(
        "INSERT INTO usuarios (username, password) VALUES (?, ?)",
        usuarios_ejemplo,
    )

    conn.commit()
    conn.close()
