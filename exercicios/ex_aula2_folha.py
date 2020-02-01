# frutas = ['abacaxi','abacate','maracuja']

# if 'caju' in frutas:
#     print('Tem caju na lita de frutas.')
# else:
#     print('Não tem caju na lista de frutas.')

# frutas.append('caju')

# if 'caju' in frutas:
#     print('Tem caju na lita de frutas.')
# else:
#     print('Não tem caju na lista de frutas.')


val_hora = int(input('Digite o valor da sua hora: \n>'))
qtd_hora = int(input('Digite a quantidade de horas trabalhadas: \n>'))

val_salario_bruto = val_hora * qtd_hora

if val_salario_bruto > 4600:
    val_desconto_ir = (val_salario_bruto * 0.27)
    val_aliquota = '27%'
elif val_salario_bruto > 3701:
    val_desconto_ir = (val_salario_bruto * 0.22)
    val_aliquota = '22%'
elif val_salario_bruto > 2801:
    val_desconto_ir = (val_salario_bruto * 0.15)
    val_aliquota = '15%'
elif val_salario_bruto > 1901:
    val_desconto_ir = (val_salario_bruto * 0.07)
    val_aliquota = '7%'
else:
    val_desconto_ir = 0.0
    val_aliquota = '0%'


val_desconto_sindicato = (val_salario_bruto * 0.03)

val_total_descontos = (val_desconto_ir + val_desconto_sindicato)

val_salario_liquido = val_salario_bruto - val_total_descontos

val_fgts = (val_salario_bruto * 0.11)


print('Valor da hora: {}'.format(val_hora))
print('Qtd de horas trabalhadas: ', qtd_hora)
print('Salario Bruto: ', val_salario_bruto)
print('(-) IR (', val_aliquota, '): ', val_desconto_ir)
print('(-) Sindicato ( 3% ):', val_desconto_sindicato)
print('FGTS:', val_fgts)
print('Total de Descontos:', val_total_descontos)
print('Salario Liquido:', val_salario_liquido)
