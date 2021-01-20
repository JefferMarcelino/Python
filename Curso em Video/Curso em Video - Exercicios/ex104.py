"""ex104 - Validando entrada de dados em Python
Crie um programa que tenha uma funcao leiaInt(), que vai funcionar de forma
semelhante a funcao input() do Python, so que fazendo a validacao para aceitar
apenas um valor numerico.
Ex:
n = leiaInt("Digite um numero")"""


def leiaInt(text):
    while True:
        b = input(text)
        if b.isnumeric():
            return b
            break
        else:
            print("\033[31mERRO! Digite um numero inteiro valido\033[m")


# PROGRAMA PRINCIPAL
n = leiaInt("Digite um numero: ")
print("Voce acabou de digitar o numero {}".format(n))
