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

# Imprimir o nome dos estados
print(dados['estados'][x]).format('rj')
# Imprimir o nome dos estados e população em Milhoes
# Imprimir o nome dos estados e qtd de municipios
