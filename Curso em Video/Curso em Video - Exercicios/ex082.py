"""ex082 - Divindo valores em varias listas
Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso,
crie duas listas extras que vao conter apenas os valores pares e os valores
impares digitados, respectivamente. Ao final, mostre o conteudo das tres listas
geradas"""

pares = []
impares = []
while True:
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    while True:
        r = str(input("Quer continuar? [S/N] ")).upper()[0]
        if r in "NS":
            break
        else:
            print("INVALIDO!")
    if r == "N":
        break
print("-=" * 30)
print("A lista completa e {}".format(pares + impares))
print("A lista de pares e {}".format(pares))
print("A lista de impares e {}".format(impares))
