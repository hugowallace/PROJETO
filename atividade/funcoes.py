import sqlite3

conn = sqlite3.connect('banco1.db')
cursor = conn.cursor()

#nao esta funcionando
def deletar_dados(tabela):
    cursor.execute(f"DELETE FROM {tabela}")
    conn.commit()


def deletar(id):
    cursor.execute(f"DELETE FROM motos_honda WHERE id = {id}")
    conn.commit()

#nao esta funcionando
def excluir_tabela(t):
    cursor.execute(f"DROP TABLE IF EXISTS {t}")
    conn.commit()


def inseir(n, p, c, cc):
    cursor.execute(f"INSERT INTO motos_honda(nome, preço, cilindrada, capacidade_combustivel) VALUES('{n}', '{p}', '{c}', '{cc}');")
    conn.commit()

#nao esta funcionando
def ver_tabelas(tabela):
    cursor.execute(f"SELECT * FROM {tabela}")
    for resultados in cursor.fectchall():
        print (resultados)


#nao esta funcionando
def ver_tabelas_id(id):
    cursor.execute(f"SELECT * FROM motos_honda WHERE id = {id}")
    for resultados in cursor.fectchall():
        print (resultados)

