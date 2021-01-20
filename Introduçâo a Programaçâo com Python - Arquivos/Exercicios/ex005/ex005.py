"""
Crie um programa que inverta a ordem das linhas do arquivo
pares.txt. A primeira linha deve conter o maior numero; e
a ultima, o menor.
"""

pares = open("../ex003/ex003 - pares.txt")
arq = open("ex005 - inverso.txt", "w")

inverso = list()
inverso.append(pares.readlines())

tam = len(inverso[0])
limite = 1

while limite != tam:
    arq.write("{}".format(inverso[0][-limite]))
    limite += 1
    if limite > tam:
        break

pares.close()
arq.close()
