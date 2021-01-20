"""ex088 - Palpites para a Mega Sena
Faca um programa que ajude um jogador da MEGA SENA a criar palpites. O programa
vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para
cada jogo, cadastrando tudo em uma lista compasta."""

from random import randint
from time import sleep

lista = []
jogos = []

print("-" * 30)
print("{:^30}".format("JOGA NA MEGA SENA"))
print("-" * 30)
quant = int(input("Quantos jogos voce quer que eu sorteie? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print("-=-=-=-= SORTEANDO {} JOGOS -=-=-=-=".format(quant))
for i, l in enumerate(jogos):
    print("Jogo {}: {}".format(i + 1, l))
    sleep(1)
print("-=" * 5, "< BOA SORTE! >", "-=" * 5)
