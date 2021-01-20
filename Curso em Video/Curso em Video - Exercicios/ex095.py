"""ex095 - Aprimorando os Dicionarios
Aprimore o DESAFIO 093 para que ele funcione com varios jogadores, incluindo,
um sistema de visualizacao de detalhes do aproveitamento de cada jogador."""

time = []
jogador = {}
gols = []

while True:
    jogador.clear()
    gols.clear()
    jogador["nome"] = str(input("Nome do Jogador: "))
    partidas = int(input("Quantas partidas o {} jogou? ".format(jogador["nome"])))
    for c in range(0, partidas):
        gols.append(int(input("    Quantos gols na partida {}? ".format(c))))
    jogador["gols"] = gols[:]
    jogador["total"] = 0
    jogador["total"] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    if resp == "N":
        break
print("-=" * 30)
print("cod ", end="")
for i in jogador.keys():
    print("{:<15}".format(i), end="")
print()
print("-" * 40)
for k, v in enumerate(time):
    print("{:>4} ".format(k), end="")
    for d in v.values():
        print("{:<15}".format(str(d)), end="")
    print()
print("-" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print("ERRO! Nao existe jogador com codigo {}!".format(busca))
    else:
        print(" -- LEVANTAMENTO DO JOGADOR {}: ".format(time[busca]["nome"]))
        for i, g in enumerate(time[busca]["gols"]):
            print("    No jogo {} fez {} gols".format(i, g))
        print("-" * 40)
print("<< VOLTE SEMPRE >>")
