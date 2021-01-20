"""ex073 - Tuplas com Times de Futebol

Crie um tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocacao. Depois mostre:

A) Os 5 primeiros.
B) Os ultimos 4 colocados.
C) Times em ordem alfabetica.
D) Em que posicao esta o time da Chapecoense."""

times = ("Corinthians", "Palmeiras", "Santos", "Gremio", "Cruzeiro",
         "Flamengo", "Vasco", "Chapecoense", "Atletico", "Botafogo",
         "Atletico-PR", "Bahia", "Sao Paulo", "Fluminense", "Sport Recife",
         "EC Vitoria", "Coritiba", "Avai", "Ponte Preta", "Atletico-Go")
print("-=" * 15)
print("Lista de times do Brasileirao: {}".format(times))
print("-=" * 15)
print("Os 5 primeiros sao {}".format(times[:5]))
print("-=" * 15)
print("Os 4 ultimos sao {}".format(times[-4:]))
print("-=" * 15)
print("Times em ordem alfabetica: {}".format(sorted(times)))
print("-=" * 15)
print("O Chapecoense esta na {}' posicao".format(times.index("Chapecoense") + 1))
