import sqlite3
from metodos import *
conn = sqlite3.connect('banco1.db')
cursor = conn.cursor()



cabecalho()
cabecalho2()
contador = 's'
while contador == 's':
    usuario = input('OPÇÃO: ').lower()
    if usuario == 'cadastrar':
        cadastrar()
        contador ='s'
    elif usuario == 'cardapio':
        cardapio()
        contador ='s'
    elif usuario == 'pedido':
        fazer_pedido()
        contador ='s'
    elif usuario == 'pesquisar':
        pesquisar()
        contador ='s'
    else:
        print('digite uma opção valida')
        contador = 's'