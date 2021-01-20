"""ex084 - Lista composta e analise de dados
Faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "NS":
            break
        else:
            print("INVALIDO!")
    if resp == "N":
        break

print("-=" * 30)
print("Ao todo voce cadastrou {} pessoas.".format(len(pessoas)))
print("O maior peso foi de {}Kg. Peso de ".format(maior), end="")
for p in pessoas:
    if p[1] == maior:
        print("{} ".format(p[0]), end="")
print()
print("O menor peso foi de {}Kg. Peso de ".format(menor), end="")
for p in pessoas:
    if p[1] == menor:
        print("{} ".format(p[0]), end="")
print()
