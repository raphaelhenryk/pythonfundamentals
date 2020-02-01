# ======================================= Métodos de String:

# texto = 'Isso é um texto'

# print(texto.upper())
# print(texto.lower())
# print(texto.capitalize())
# print(texto.split(' '))

# ======================================= Tuplas

# valores = (1, 2, 3, 4, [10, 20, 30], 'teste')
# print(valores)

# ======================================= Dicionarios

# ling_favorita = {'João': 'Java', 'Raphael': 'Python', 'Marcelo': 'php', /
# 'Pedro': 'Shell Script'}
# print(ling_favorita['Raphael'])

# ling_favorita['Raphael'] = 'SQL'
# print(ling_favorita['Raphael'])

# ling_favorita.update({'Pedro':'Ajax'})
# print(ling_favorita)

dados_clientes = {'clientes': {'cl001': {'nome': 'Raphael Santos', 'idade': 26, 'telefone': '21971114902'},
                               'cl002': {'nome': 'Pedro Santos', 'idade': 23, 'telefone': '21972212760'}
                               }
                  }

print(dados_clientes['clientes']['cl002']['nome'],
      dados_clientes['clientes']['cl002']['telefone'])

codigo_cliente = input('Digite o codigo do cliente: ')
print(dados_clientes['clientes'][codigo_cliente])


# ======================================= Trataento de Exceções com while

lista_logins = {'Raphael': '123456', 'Renan': '45678'}

while True:
    try:
        user_login = input('Digite o nome de usuário: \n>')
        if user_login not in lista_logins:
            print('Usuário ', user_login, ' nao cadastrado.')
            break
        else:
            raise Exception('Usuario  não Cadastrado')
            continue
    except Exception as e:
        print(e)
