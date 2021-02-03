from math import sqrt


def leianum(msg):
    while True:
        num = str(input(msg))
        try:
            int(num)
            return int(num)
        except:
            print("Invalido!", end=" ")


n = leianum("Digite um numero > ")

print("-=" * 15)
print("Dados sobre o numero {}".format(n).center(30))
print("-=" * 15)

print("> Dobro: \t\t\t{}".format(n * 2))
print("> Triplo: \t\t\t{}".format(n * 3))
print("> Metade: \t\t\t{}".format(n / 2))
print("> Posicao: \t\t\t{}ª posicao".format(n))
print("> Raiz Quadrada: \t{}".format(sqrt(n)))
