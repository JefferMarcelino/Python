"""ex103 - Ficha de Jogador
Faca um programa que tenha chamada ficha(), que receba dois parametros opcionais:
o nome de jogador e quantos gols ele marcou. O programa devera ser capaz de mostrar
a ficha do jogador, mesmo que algum dado nao tenha sido informado correctamente."""


def jogador(n, g):
    if n == "":
        n = "<desconhecido>"
    if not g.isnumeric():
        g = 0
    print("O jogador {} fez {} gols(s) no campeonato.".format(n, g))


# PROGRAMA PRINCIPAL
print("-" * 30)
nome = str(input("Nome do Jogador: ")).strip()
gols = str(input("Numero de Gols: "))
jogador(nome, gols)
