"""
Crie um programa que leia os arquivos ex003 - pares.txt e
ex003 - impares.txt e que crie so um arquivo ex003 - pare
seimpares.txt com todas as linhas dos outros dois arquivos,
de forma a preservar a ordem numerica.
"""

pares = open("ex003 - pares.txt")
impares = open("ex003 - impares.txt")
pareseimpares = open("ex003 - pareseimpares.txt", "w")
ordem = []

for linha in pares.readlines():
    ordem.append(int(linha))

for linha in impares.readlines():
    ordem.append(int(linha))

ordem.sort()

for linha in ordem:
    pareseimpares.write("{}\n".format(linha))

pares.close()
impares.close()
pareseimpares.close()
