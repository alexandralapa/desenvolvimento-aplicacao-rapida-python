import sqlite3

def conectar_db():
    db_connection = sqlite3.connect("usuarios.db")
    cursor = db_connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            nome TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    """)
    db_connection.commit()
    db_connection.close()