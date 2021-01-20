"""ex088 - Boletim com listas compostas
Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a media de cada um e permita que o usuario
possa mostar as notas de cada aluno individualmente"""

ficha = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "NS":
            break
        else:
            print("INVALIDO")
    if resp == "N":
        break

print("-=" * 30)
print("{:<4}{:<10}{:>8}".format("No.", "NOME", "MEDIA"))
print("-" * 26)

for i, a in enumerate(ficha):
    print("{:<4}{:<10}{:>8.1f}".format(i, a[0], a[2]))

while True:
    print("-" * 35)
    opc = int(input("Mostar notas de qual aluno? (999 interrope): "))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print("Notas de {} sao {}".format(ficha[opc][0], ficha[opc][1]))

print("<<< VOLTE SEMPRE >>>")
