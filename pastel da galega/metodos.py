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



def pesquisar():
    p = input('Digite o nome do cliente: ').lower()
    s = cursor.execute(f"SELECT * FROM clientes WHERE nome = '{p}'" )
    for x in cursor.fetchall():
        print(x)


# def atualizar():
#     print('ATUALIZANDO CADASTRO DE CLIENTES!!!exit \nNome\nEndereço\nTelefone\nEXIT  para sair')
#     atualizador = input('Oque deseja atualizar ?').lower()
#     while atualizador not in 'exit':
#         if atualizador == 'nome':
#             nome = input('Digite o nome do cliente que deseja atualizar: ')
#         elif atualizador == 'endereço':
#             endereço = input('Digite o endereço do cliente que deseja atualizar: ')
#         elif atualizador == 'telefone':
#             telefone = input('Digite o telefone do cliente que deseja atualizar: ')
#         else:
#             atualizador = input('Digite nome, endereço ou telefone para atualizar alguma coisa!').lower()


def dropar():
    cursor.execute(f"DROP TABLE produto")