lista_logins = {'Raphael': '123456', 'Renan': '45678'}

user_login = input('Digite o nome de usuário: \n>')
if user_login not in lista_logins:
        print('Usuário ', user_login, ' nao cadastrado.')
else:
        user_password = input('Digite a senha: \n>')
        if lista_logins[user_login] == user_password:
            print('Acesso Válido. Seja Bem vindo.')
        else:
            print('Acesso Negado. Tente outra vez.')
