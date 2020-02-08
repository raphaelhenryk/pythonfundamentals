lista_logins = {'raphael': '123', 'renan': '456'}
while True:
    try:
        user_login = input('Digite o nome de usuário: \n>')
        if user_login.lower() not in lista_logins:
            raise Exception('Usuario  não Cadastrado')
            continue
        else:
            user_password = input('Digite a senha: \n>')
            if lista_logins[user_login.lower()] == user_password:
                print('Acesso Válido. Seja Bem vindo.')
                break
            else:
                raise Exception('Senha Incorreta.')
                continue
    except Exception as e:
        print(e)
    finally:
        print("Conexao Fechada com o Banco")
