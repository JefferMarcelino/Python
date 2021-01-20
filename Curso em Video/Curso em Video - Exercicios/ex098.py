"""Faca um programa que tenha uma funcao chamada contador(), que receba tres
parametros: inicio, fim e passo. Seu programa tem que realizar tres contagens
atraves de funcao criada:
A)De 1 ate 10, de 1 em 1.
B)De 10 ate 0, de 2 em 2.
C)Uma contagem personalizada."""

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("Contagem de {} ate {} de {} em {}".format(inicio, fim, passo, passo))
    sleep(2.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=" ", flush=True)
            sleep(0.5)
            cont += passo
        print("FIM!")
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=" ", flush=True)
            sleep(0.5)
            cont -= passo
        print("FIM!")
    print("-=" * 30)


contador(1, 10, 1)
contador(10, 0, 2)

print("Agora e sua vez de personalizar a contagem!")
i = int(input("Inicio: "))
f = int(input("Fim:    "))
p = int(input("Passo:  "))
contador(i, f, p)
