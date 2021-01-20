"""ex099 - Funcao que descobre o maior
Faca um programa que tenha um funcao chamada maior(), que receba varios
parametros com valores inteiros. Seu programa tem que analisar todos os valores
e dizer qual deles e o maior."""

from time import sleep


def maior(*nums):
    mai = cont = 0
    print("Analisando os valores passados...")
    for numero in nums:
        print(numero, end=" ")
        sleep(0.5)
    print("Foram informados {} valores ao todo.".format(len(nums)))
    for numero in nums:
        if cont == 0:
            mai = numero
        else:
            if mai < numero:
                mai = numero
        cont += 1
    print("O maior valor foi {}.".format(mai))
    print("-=" * 30)


# PROGRAMA PRINCIPAL
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
maior(10, 125, 15, 8, 0)
