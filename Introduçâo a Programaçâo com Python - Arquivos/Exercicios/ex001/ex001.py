"""
Escreva um programa que receba o nome de um arquivo pela
linha de comando e que imprima todas as linhas desse arquivo."""

nome = str(input("Digite o nome do arquivo: "))

try:
    arq = open(nome+".txt", "r")
except FileNotFoundError:
    arq = open(nome+".py", "r")

for linha in arq.readlines():
    print(linha)
arq.close()
