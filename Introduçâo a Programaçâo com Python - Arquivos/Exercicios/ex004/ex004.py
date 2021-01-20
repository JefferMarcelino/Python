"""
Crie um programa que receba o nome de dois arquivos como
parametros da linha de comando e que gere um arquivo de
saida com as linhas do primeiro e do segundo arquivo.
"""

nome1 = str(input("Nome do primeiro arquivo: "))
nome2 = str(input("Nome do segundo arquivo: "))

arq1 = open(nome1)
arq2 = open(nome2)
arq3 = open("ex004 - Arquivo de saida.txt", "w")

for linha in arq1.readlines():
    arq3.write("{}".format(linha))

arq3.write("\n")
arq3.write("\n")
arq3.write("\n")

for linha in arq2.readlines():
    arq3.write("{}".format(linha))

arq1.close()
arq2.close()
arq3.close()
