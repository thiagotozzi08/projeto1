import sqlite3

class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

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

def delete_note(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM note WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def get_note(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM note WHERE id = ?", (id,))
    linha = cursor.fetchone()
    conn.close()
    return Note(linha['id'], linha['title'], linha['content'])

def update_note(id, title, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE note SET title = ?, content = ? WHERE id = ?", (title, content, id))
    conn.commit()
    conn.close()