import sqlite3

conn = sqlite3.connect('banco1.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE clientes(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    endereço TEXT
);""")

