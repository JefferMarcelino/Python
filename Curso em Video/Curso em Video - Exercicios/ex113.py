"""ex113 - Funcoes aprofundadas em Python"""


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero inteiro valido.\033[m")
            continue
    return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            break
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero real valido.\033[m")
            continue
    return n


n1 = leiaInt("Digite um numero inteiro: ")
n2 = leiaFloat("Digite um numero real: ")

print("O valor inteiro digitado foi {} e o real foi {}".format(n1, n2))
