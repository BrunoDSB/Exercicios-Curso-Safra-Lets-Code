import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    ...
    categorias = []
    for i in range(0, len(dados)):
        if not(dados[i]['categoria'] in categorias):
            categorias.append(dados[i]['categoria'])
    return categorias
    # for elemento in categorias:
    #     print(elemento.title())


def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    ...
    lista_categoria = []
    for i in range(0, len(dados)):
        if dados[i]['categoria'] == categoria:
            lista_categoria.append(dados[i])
    lista_categoria = sorted(lista_categoria, key = lambda x:float(x["preco"]), reverse = True)
    return lista_categoria
    # for elemento in lista_categoria:
    #     print(elemento)
    

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...
    lista_mais_caro = []
    for i in range(0, len(dados)):
        if dados[i]['categoria'] == categoria:
            lista_mais_caro.append(dados[i])
    lista_mais_caro = sorted(lista_mais_caro, key = lambda x:float(x["preco"]), reverse = True) [:1]
    return lista_mais_caro
    # print(f'O Produto mais caro da categoria "{categoria.title()}" é:\n', lista_mais_caro)




def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...
    lista_mais_barato = []
    for i in range(0, len(dados)-1):
        if dados[i]['categoria'] == categoria:
            lista_mais_barato.append(dados[i])
    lista_mais_barato = sorted(lista_mais_barato, key = lambda x:float(x["preco"])) [:1]
    return lista_mais_barato
    # print(f'O Produto mais barato da categoria "{categoria.title()}" é:\n', lista_mais_barato)

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    ...
    top_caros = sorted(dados, key = lambda x:float(x["preco"]), reverse = True) [:10]
    return top_caros

    # for i in dados_organizados:
    #     print (i)

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    ...
    top_baratos = sorted(dados, key = lambda x:float(x["preco"])) [:10]
    return top_baratos
    # for i in dados_organizados:
    #     print (i)

def categoria_validar(categoria):

    categorias = listar_categorias(dados)
    while categoria not in categorias:
        print("A categoria digitada, não foi encontrada em nosso banco de dados!")
        categoria = input('Insira uma nova categoria desejada:').lower()
    else:
        return categoria

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    ...
    print('''\nMenu Interativo
        Abaixo segue lista de opções para iniciar sua pesquisa:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair\n''')
    opcao = input('Digite o número da opção desejada: ')
    print()
    opcoes = ['0', '1', '2', '3', '4', '5', '6']
    while not (opcao == '0'):
        while not (opcao.isdigit() and opcao in opcoes):
            print('''\n Você digitou uma opção inválida!
        Abaixo segue lista de opções válidas:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair\n''')
            opcao = input('Qual opção você deseja escolher? ')
            print()
        else:

            if opcao == '1':
                for i in listar_categorias(dados):
                    print(i.title())

            elif opcao == '2':
                categoria = input('\nQual categoria você deseja escolher? ').lower()
                categoria = categoria_validar(categoria)
                lista_categoria = listar_por_categoria(dados, categoria)
                print(f"\nA categoria escolhida foi: {categoria.title()}")
                for i in range(0, len(lista_categoria)):
                    print(f"\n Id: {lista_categoria[i]['id']} \n Preço: R$ {lista_categoria[i]['preco']}")

            elif opcao == '3':
                categoria = input('\nQual categoria você deseja escolher? ').lower()
                categoria = categoria_validar(categoria)
                lista_caro = produto_mais_caro(dados, categoria)
                print(f"\nA categoria escolhida foi: {categoria.title()}")
                for i in range(0, len(lista_caro)):
                    print(f"O produto mais caro é o id: {lista_caro[i]['id']}. \nNo valor de R$ {lista_caro[i]['preco']}")

            elif opcao == '4':
                # categoria = input('\nQual categoria você deseja escolher? ').lower()
                # produto_mais_barato(dados, categoria)
                categoria = input('\nQual categoria você deseja escolher? ').lower()
                categoria = categoria_validar(categoria)
                lista_barato = produto_mais_barato(dados, categoria)
                print(f"\nA categoria escolhida foi: {categoria.title()}")
                for i in range(0, len(lista_barato)):
                    print(f"O produto mais caro é o id: {lista_barato[i]['id']}. \nNo valor de R$ {lista_barato[i]['preco']}")

            elif opcao == '5':
                top_caros = top_10_caros(dados)
                print(f"\nOs 10 produtos mais caros são: ")
                for i in range(0, len(top_caros)):
                    print(f"\n Id: {top_caros[i]['id']} \n Preço: R$ {top_caros[i]['preco']} \n Categoria: {top_caros[i]['categoria']} ")

            elif opcao == '6':
                top_baratos = top_10_baratos(dados)
                print(f"\nOs 10 produtos mais baratos são: ")
                for i in range(0, len(top_baratos)):
                    print(f"\n Id: {top_baratos[i]['id']} \n Preço: R$ {top_baratos[i]['preco']} \n Categoria: {top_baratos[i]['categoria']} ")

        print()
        opcao = input('\nQual a proxima opção desejada? ')
    print('\nObrigado! Até a próxima!')

# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)

