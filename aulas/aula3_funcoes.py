# produtos = []

# def cadastraProduto(produto):
#     #pega a variavel global que está fora do escopo da função
#     global produtos
#     produtos.append(produto)

# def calculaSoma(x,y):
#     print('Total da soma: \n', x+y)

# def calculaSubtracao(x,y):
#     print('Total da subtracao: \n', x-y)

# x = int(input('Digite o valor de x: \n >'))
# y = int(input('Digite o valor de y: \n >'))

# calculaSoma(x,y)
# calculaSubtracao(x,y)


# def imprimeMaior(value1, value2):
#     text = 'O maior numero é: '
#     if value1 > value2:
#         print(text, value1)
#     else:
#         print(text, value2)


# x = int(input('Digite o valor de x: \n >'))
# y = int(input('Digite o valor de y: \n >'))
# imprimeMaior(x, y)


# def maior(*valores):
#     print(sorted(valores))

# n1 = [1, 2, 65, 4, 3, 2, 7, 85, 99]
# maior(1, 2, 65, 4, 3, 2, 7, 85, 99)


# def ordena(*valores):
#     return sorted(valores)

# t = ordena(1, 2, 65, 4, 3, 2, 7, 85, 99)
# print(t)


# import requests

# def api(**valores):
#     req = requests.get(valores['URL'])
#     print(valores)
#     return req

# print(api(URL='https://www.google.com', code_status='valor_esperado_200', retorno='ok'))


# ======================================= Funções Lambda
# Funçoes decartáveis.
# sub2 = lambda x, y: x - y

# sub2(10, 8)


# ======================================= Função Map
# lista = [1,2,3,4,5,6]
# dobro = list(map(lambda x: x*2, lista))
# print(dobro)

# ======================================= Função Reduce
# from functools import reduce
# lista = [1, 2, 3, 4, 5, 6]
# soma = reduce(lambda x, y: x + y, lista)
# print(soma)


# ======================================= Função Filter
# lista = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]

# n_par = list(filter(lambda x: x % 2 == 0, lista))
# print(n_par)
