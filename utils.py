import sqlite3

def load_template(nome_arquivo):
    caminho = f"static/templates/{nome_arquivo}"
    with open(caminho, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    return conteudo

def get_connection():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_notes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM note")
    notas = cursor.fetchall()
    conn.close()
    return notas

def add_note(title, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO note (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()