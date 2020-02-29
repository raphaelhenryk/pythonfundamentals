def somar(x,y):
    return x + y

def subtrair(x,y):
    return x - y

def multiplicar(x,y):
    return x * y

def dividir(x,y):
    return x / y

assert somar(2, 2) == 4, "Obtido: {}, Esperado: 4".format(somar(2, 2))
assert somar(3, 3) == 6, "Obtido: {}, Esperado: 6".format(somar(3, 3))

assert subtrair(2, 2) == 0, "Obtido: {}, Esperado: 0".format(subtrair(2, 2))
assert subtrair(2, 2) == 4, "Obtido: {}, Esperado: 4".format(subtrair(2, 2))

assert multiplicar(2, 2) == 4, "Obtido: {}, Esperado: 4".format(multiplicar(2, 2))
assert multiplicar(2, 2) == 4, "Obtido: {}, Esperado: 4".format(multiplicar(2, 2))

assert dividir(2, 2) == 4, "Obtido: {}, Esperado: 4".format(dividir(2, 2))
assert dividir(2, 2) == 4, "Obtido: {}, Esperado: 4".format(dividir(2, 2))