import sqlite3
conn = sqlite3.connect('banco1.db')
cursor = conn.cursor()



def cabecalho():
    print('#'*20)
    print('##PASTEL DA GALEGA##')
    print('#### DELIVERY ######')
    print('#'*20)

def cadastrar():
    nome = input('nome do cliente: ')
    telefone = input('telefone do cliente: ')
    endereço = input('enredeço do cliente: ')
    cursor.execute(f"INSERT INTO clientes (nome, telefone, endereço) VALUES('{nome}', '{telefone}', '{endereço}');")
    conn.commit()
