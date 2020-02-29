from unittest import TestCase, main

# 1 Dado ma função que a principio nao faz nada
# quero validar se a entrada tem que ser inteiro, e a saida sera forcada como booleano


def valida_par(num: int) -> bool:
    if isinstance(num, int):
        return True if num % 2 == 0 else False
    elif isinstance(num, str):
        if num.isnumeric():
            return True if int(num) % 2 == 0 else False
        else:
            return None

class Testes(TestCase):
    def test_par(self):
        self.assertEqual(valida_par(4), True)
    def test_impar(self):
        self.assertEqual(valida_par(5), False)
    def test_string(self):
        self.assertEqual(valida_par('102'), True)
        self.assertEqual(valida_par('string'), None)

if __name__ == "__main__":
    main()