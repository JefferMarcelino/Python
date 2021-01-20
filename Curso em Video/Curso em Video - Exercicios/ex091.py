"""ex091 - Jogo de Dados em Python
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde
esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo que
o vencedor tirou o maior numero no dado."""

from random import randint
from time import sleep
from operator import itemgetter

jogo = {"jogador1": randint(0, 6),
        "jogador2": randint(0, 6),
        "jogador3": randint(0, 6),
        "jogador4": randint(0, 6)}
ranking = []
print("Valores sorteados:")
for k, v in jogo.items():
    print("{} tirou {} no dado".format(k, v))
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("-=" * 30)
print("== RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print("{}o lugar: {} com {}.".format(i + 1, v[0], v[1]))
    sleep(1)
