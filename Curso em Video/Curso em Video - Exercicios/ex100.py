"""ex100 - Funcoes para sortear e somar
Faca um programa que tenha uma lista chamada numeros e duas funcoes chamadas
sorteia() e somaPar(). A primeira funcao vai sortear 5 numeros e vai coloca-los
dentro da lista e a segunda funcao vai mostar a soma entre todos os valores
PARES sorteados pela funcao anterior."""

from random import randint
from time import sleep
numeros = []


def sorteia():
    print("Sorteado 5 valores da lista: ", end="")
    for c in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)
        print(n, end=" ")
        sleep(0.3)
    print("PRONTO!")


def pares(lst):
    par = 0
    for cada in lst:
        if cada % 2 == 0:
            par += cada
    print("Somando os valores pares de {}, temos {}".format(numeros, par))


sorteia()
pares(numeros)
