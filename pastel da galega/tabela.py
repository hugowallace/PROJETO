import sqlite3
import datetime
conn = sqlite3.connect('banco1.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE clientes(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    endereço TEXT
);""")

cursor.execute("""CREATE TABLE pedido(
    id_pedido INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    data_compra TEXT,
    FOREIGN KEY (id_cliente) REFERENCES clientes (id)     
);""")

cursor.execute("""CREATE TABLE produto(
    id_produto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    sabor1 TEXT DEFAULT '',
    sabor2 TEXT DEFAULT '',
    sabor3 TEXT DEFAULT '',
    sabor4 TEXT DEFAULT '',
    sabor5 TEXT DEFAULT '',
    preço text
);""")


cursor.execute("""CREATE TABLE item_pedido(
    id_pedido INTEGER,
    id_produto INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produto (id_protudo)
);""")