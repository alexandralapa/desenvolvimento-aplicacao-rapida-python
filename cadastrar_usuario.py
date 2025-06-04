import sqlite3
from gerar_senha import gerar_hash

def cadastrar_usuario(usuario, nome, senha):
    db_connection = sqlite3.connect("usuarios.db")
    cursor = db_connection.cursor()
    senha_hash = gerar_hash(senha)
    try:
        cursor.execute("INSERT INTO usuarios (usuario, nome, senha) VALUES (?, ?, ?)", (usuario, nome, senha_hash))
        db_connection.commit()
        db_connection.close()
        return True
    except sqlite3.IntegrityError:
        db_connection.close()
        return False