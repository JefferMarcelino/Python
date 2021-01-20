"""ex072 - Numero por extenso
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero ate vinte.

Seu programa devera ler um numero pelo teclado(entre 0 e 20)
e mostra-lo por extenso."""

numeros = ("zero", "um", "dois", "tres", "quatro", "cinco",
           "seis", "sete", "oito", "nove", "dez", "onze",
           "doze", "treze", "catorze", "quinze", "dezesseis",
           "dezesete", "dezoito", "dezenove", "vinte")
N = int(input("Digite um numero entre 0 e 20: "))
while True:
    if N < 0 or N > 20:
        N = int(input("INVALIDO! Digite um numero entre 0 e 20: "))
    else:
        break

print("Voce digitou o numero {}".format(numeros[N]))
