
# Repeticao

# frutas = ['Abacaxi', 'Banana', 'Caju']

# for fruta in frutas:
#     print(fruta)

# Range (1, 100: não inclusivo = 99)

# itens = []
# for item in range(0, 101, 2):
#     itens.append(item)

# print(itens)

# carros = ['gol', 'corsa', 'fox']
# cores = ['prata', 'vermelho', 'branco']

# for carro in carros:
#     for cor in cores:
#         print(carro, cor)


# frutas = ['Abacaxi', 'Banana', 'Caju']
# x = enumerate(frutas)

# for i,f in x:
#     print(i,f)


# O bloco finally, se especificado, será executado independente de surgir ou não um erro no try


# try:
#     a = int(input('Diga-me um número: '))
#     b = int(input('Diga-me um outro número: '))
#     print("a/b = ", a/b)
#     print("a+b = ", a+b)
#     break
# except ValueError:  # Só executa se esse erro surgir
#     print('Não podemos converter para um número')
# except ZeroDivisionError:  # Só executa se esse erro surgir
#     print('Não podemos dividir por zero')
# except:  # executa para todos os outros erros
#     print('algo de muito errado aconteceu')
# finally:
#     print("Conexao Fechada com o Banco")




# ======================================= Trabalhando com arquivos

with open('arquivo.txt', 'w') as f:
    f.write('Novo arquivo .txt')

    
