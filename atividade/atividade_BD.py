import sqlite3

conn = sqlite3.connect('banco1.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE motos_honda (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preço TEXT,
    cilindrada TEXT,
    capacidade_combustivel TEXT
);""")

cursor.execute("""INSERT INTO motos_honda(nome, preço, cilindrada, capacidade_combustivel)
    VALUES('Biz', 'A partir de R$ 10.481', '124,9 cc', ' 5,1 litros'),
          ('CG 160 Cargo', 'A partir de 10.703', '162,7 cc', '16,1 litros'),
          ('CG 160 Start', 'A partir de R$ 9.444','162,7 cc', '14,6 litros'),
          ('CG 160 Titan S', 'A partir de R$ 12.188', '162,7 cc', '16,1 litros');""")
conn.commit()
conn.close()
