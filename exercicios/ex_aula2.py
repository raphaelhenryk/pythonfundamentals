# _*_ coding:utf-8 _*_

dados = {
    'estados': {
        'sp': {
            'nome': 'São Paulo',
            'municipios': 645,
            'população': 44.04
        },
        'rj': {
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'população': 16.72
        },
        'mg': {
            'nome': 'Minas Gerais',
            'municipios': 31,
            'população': 20.87
        }
    }
}

# uf = input('Digite o nome do estado:'.lower())

# nome_sp = dados['estados']['sp']['nome']
# nome_rj = dados['estados']['rj']['nome']
# nome_mg = dados['estados']['mg']['nome']

# print(f'O nome dos estados são: {nome_sp}, {nome_rj}, {nome_mg}')
# #ou
# print('O nome dos estados são:{}, {}, {}'.format(nome_sp, nome_rj, nome_mg))

# Imprimir o nome dos estados (loop)
x = ['sp', 'rj', 'mg']

for i in x:
    print(dados['estados'][i]['nome'])

# Imprimir o nome dos estados e população em Milhoes
for i in x:
    print('O ESTADO ', dados['estados'][i]['nome'], ' POSSUI ',
          dados['estados'][i]['população'], ' Milhões de Habitantes')

# Imprimir o nome dos estados e qtd de municipios
for i in x:
    print('O ESTADO ', dados['estados'][i]['nome'], ' POSSUI ',
          dados['estados'][i]['municipios'], ' municipios.')


# ====================================== Condicionais
