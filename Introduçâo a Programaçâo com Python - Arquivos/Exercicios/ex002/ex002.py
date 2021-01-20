"""
Modifique o programa ex001 para que receba mais dois
parametros: a linhas de inicio e a de fim para imprensao.
O programa deve imprimir apenas as linhas entre esses dois
valores (incluindo as linhas inicio e fim).
"""


nome = str(input("Digite o nome do arquivo: "))
inicio = int(input("Digite a linha de inicio: "))
fim = int(input("Digite a linha de fim: "))
print("-=" * 15)
cont = 0

try:
    arq = open(nome+".txt", "r")
except FileNotFoundError:
    arq = open(nome+".py", "r")

for linha in arq.readlines():
    cont += 1
    if fim >= cont >= inicio:
        print(linha)
