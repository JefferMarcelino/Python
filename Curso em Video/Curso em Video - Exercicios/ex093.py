"""ex093 - Cadastro de Jogador de Futebol
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai
a quantidade de gols feitos em cada partida. No final, tudo isso sera guardado
em um dicionario, incluido o total feitos durante o campeonato."""

jogador = {}
gols = []
jogador["nome"] = str(input("Nome do Jogador: "))
partidas = int(input("Quantas partidas o {} jogou? ".format(jogador["nome"])))
for c in range(0, partidas):
    gols.append(int(input("    Quantos gols na partida {}? ".format(c))))
jogador["gols"] = gols[:]
jogador["total"] = 0
jogador["total"] = sum(gols)
print("-=" * 30)
print(jogador)
print("-=" * 30)
for k, v in jogador.items():
    print("O campo {} tem o valor {}".format(k, v))
print("-=" * 30)
print("O jogador {} jogou {} partidas.".format(jogador["nome"], partidas))
for e, cada in enumerate(gols):
    print("    => Na partida {}, fez {} gols".format(e, cada))
print("Foi um total de {} gols".format(jogador["total"]))
