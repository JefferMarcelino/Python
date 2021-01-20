"""
Crie um programa que receba uma lista de nomes de um arquivo e os
imprima um por um.
"""

arq = open("ex009 - lista de nomes.txt")

for linha in arq.readlines():
    print(linha.replace("[", "").replace("]", "").replace("\"", "")
          .replace(",", "").replace(" ", "\n"), end="")

arq.close()
