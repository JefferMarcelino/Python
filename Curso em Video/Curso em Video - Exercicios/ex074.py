"""ex074 - Maior e menor valores em Tupla
Crie um programa que vai gerar cinco numeros aleatorios e
colocar em uma tupla. Depos disso, mostre a listagem de
numeros gerados e tambem indique o menor e o maior valor que
estao na tupla"""

from random import randint

sorteados = (randint(0, 10), randint(0, 10), randint(0, 10),
             randint(0, 10), randint(0, 10))
print("Os valores sorteados foram: {}".format(sorteados))
print("O maior valor sorteado foi {}".format(max(sorteados)))
print("O menor valor sorteado foi {}".format(min(sorteados)))
