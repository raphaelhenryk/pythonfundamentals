# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# n3 = float(input('Digite a terceira nota: '))
# n4 = float(input('Digite a quarta nota: '))

# nfinal = (n1+n2+n3+n4)/4
# print(nfinal)


# TESTANTO O .format

# n1 = str(input('Digite o seu nome: '))
# n2 = str(input('Digite o se sobrenome: '))
# n3 = str(input('Digite o nome do seu dog: '))

# print('{} {}, o {} está com fome.'.format(n1,n2,n3))

palavra = 'Raphael Henryk da Silva Santos'
print(palavra.upper())
print(palavra.split())
print(palavra.capitalize())
print(palavra.replace('a','e',))



# listas

# lista = ['abacaxi', 503, 50.9, [1, 2, 3, 4, [5, 6, 7, [8, 9]]]]

# print(lista[3])
# print(lista[3][4])
# print(lista[3][4][3])



lista = ['Corinthians', [1, 2, 3, 4, 5], 'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14], 'Flamengo', 'Vasco']
# print 3, 13, vasco
print(lista[1][2], lista[4][3], lista[6])
# print 4, São Paulo, 14
print(lista[1][3], lista[3], lista[4][4])
# print Corinthians, 2, 10, 14
print(lista[0], lista[1][1], lista[4][0], lista[4][4])

#pega o ultimo
print(lista[-1])

#pega o peultimo
print(lista[-2])

#testes
# : dois pontos representa toda a lista. Primeiro item é incluído, e a partir do segundo é excluído
print(lista[:3])

print(lista[3:4])

#index
print(lista.index('Vasco'))