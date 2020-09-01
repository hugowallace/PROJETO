import sqlite3
conn = sqlite3.connect('banco1.db')
cursor = conn.cursor()


def cabecalho2():
    print("""
Digite:
CADASTRAR para cadastrar cliente;
CARDAPIO para ver o cardapio;
PEDIDO para fazer um pedido;
PESQUISAR para pesquisar dados do cliente;
S para sair.""")

def cabecalho():
    print('#'*20)
    print('PASTEL DA GALEGA'.center(20))
    print('DELIVERY'.center(20))
    print('#'*20)

def cadastrar():
    nome = input('nome do cliente: ')
    telefone = input('telefone do cliente: ')
    endereço = input('enredeço do cliente: ')
    cursor.execute(f"INSERT INTO clientes (nome, telefone, endereço) VALUES('{nome}', '{telefone}', '{endereço}');")
    conn.commit()
def cadastrar_produtos():
    produto = input('nome do produto: ')


def pesquisar():
    p = input('Digite o nome do cliente: ')
    s = cursor.execute(f"SELECT * FROM clientes WHERE nome LIKE '%{p}%'" )
    for x in cursor.fetchall():
        print(x)
    

def cardapio():
    print("""
        PASTÉIS                                             SALGADOS
    3 sabores----------------->R$4,00       Coxinha de frango---------------->R$3,50
    5 sabores----------------->R$6,00       Coxinha de frango com catupiry--->R$3,50
    Sò charque pequeno-------->R$5,00       Coxinha de charque--------------->R$4,00
    Só charque grande--------->R$7,00       Coxinha de charque com catupiry-->R$4,00
    Só carne de sol pequeno--->R$5,00       Enroladinho---------------------->R$3,00
    Só carne de sol grande---->R$7,00       Pastelão (fatia)----------------->R$4,00
    BEBIDAS                                 Cachorro quente------------------>R$3,00
    Refrigerante 200mL-------->R$2,00                       DOCES
    Refrigerante lata 350mL--->R$4,00       Bolo (fatia)--------------------->R$4,00
    Regrigerante de 1Litro---->R$6,00       Bolo de pote--------------------->R$4,00
    Refrigerante de 2Litros--->R$9,00       Tortinha Doce-------------------->R$1,00
    Suco da polpa------------->R$4,00       Torta de limao (fatia)----------->R$4,00
                                            Mousse--------------------------->R$3,00
                                    

    SOBORES DOS PASTÉIS              ACOMPANHAMENTOS
    
    FRANGO                              CENOURA
    CARNE DE SOL                        TOMATE E CEBOLA
    QUEIJO CHEDDAR                      MILHO E ERVILHA
    QUEIJO MUSSARELA                    ORÉGANO
    QUEIJO COALHO                       CATCHUP
    CATUPIRY                            MAIONESE
    CHARQUE                             MOSTARDA
    CARNE MOÍDA                         BARBECUE
    BACON                               MOLHO DE PIMENTA
    CREME DE CAMARÃO                    MOLHO DE ALHO
    CREME DE FRANGO                     OVO DE CODORNA
    """)

def fazer_pedido():
    nome = input('Nome do cliente: ')
    id_cliente = input('ID do cliente: ')
    print('DIGITE UM ITEM POR VEZ')
    cd_item = 1
    contador = 'sim'
    while contador == 'voltar':
        pedido = input(f'ITEM {cd_item}: ').lower()
        cd_item =+ 1
        if pedido == 'pastel':
            qtdsabor = int(input('pastel de 5 ou 3  sabores? '))
            q = 1
            if qtdsabor == 3:
                for x in range(3):
                    x = input(f'Sabor {q}: ')
                    q += 1
            elif qtdsabor == 5:
                for x in range(5):
                    x = input(f'Sabor {q}')
                    q += 1
            else:
                print('Só temos pasteis de 5 ou 3  sabores!!!!')
            cd_item =+ 1
        elif pedido == 'coxinha':
            sabor_coxinha = input('Sabor: ')
            qtdcoxinha = int(input('Quantidade: '))
           
            cd_item =+ 1
        elif pedido == 'cachorro quente':
            cachorro_quente = input('completo? ')
            
            cd_item =+ 1
        elif pedido == 'enroladinho':
            enroladinho = input('completo? ')
            cd_item =+ 1
        else:
            print(f'não temos {pedido} tente outra coisa')
            contador = input('deseja sair ? ')   
            cd_item =+ 1
    # print('ATUALIZANDO CADASTRO DE CLIENTES!!!exit \nNome\nEndereço\nTelefone\nEXIT  para sair')
    # atualizador = input('Oque deseja atualizar ?').lower()
    # while atualizador not in 'exit':
    #     if atualizador == 'nome':
    #         nome = input('Digite o nome do cliente que deseja atualizar: ')
    #     elif atualizador == 'endereço':
    #         endereço = input('Digite o endereço do cliente que deseja atualizar: ')
    #     elif atualizador == 'telefone':
    #         telefone = input('Digite o telefone do cliente que deseja atualizar: ')
    #     else:
    #         atualizador = input('Digite nome, endereço ou telefone para atualizar alguma coisa!').lower()


def dropar():
    cursor.execute(f"DROP TABLE motos_honda")