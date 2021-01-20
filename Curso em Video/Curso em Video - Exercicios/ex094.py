"""ex094 - Unindo dicionarios e listas
Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os
dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
No final, mostre:
A) Quantas pessoas cadastradas.
B) A media de idade.
C) Uma lista com mulheres.
D) Uma lista de com idade acima da media."""

dados = []
pessoas = {}
idade = 0
mulheres = []
while True:
    pessoas["nome"] = str(input("Nome: ")).title()
    while True:
        sexo = str(input("Sexo: [F/M] ")).upper()[0]
        if sexo == "F":
            mulheres.append(pessoas["nome"])
        if sexo in "MF":
            break
        else:
            print("ERRO! Por favor, digite apenas M ou F.")
    pessoas["sexo"] = sexo
    pessoas["idade"] = int(input("Idade: "))
    idade += pessoas["idade"]
    dados.append(pessoas.copy())
    pessoas.clear()
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "NS":
            break
        else:
            print("ERRO! Responda apenas S ou N.")
    if resp == "N":
        break
print("-=" * 30)
print("A) Ao todo temos {} pessoas cadastradas.".format(len(dados)))
print("B) A media de idade e de {} anos".format(idade / len(dados)))
print("C) As mulheres cadastradas foram ", end="")
for cmulher in mulheres:
    print(cmulher, end=" ")
print("\nD) Lista das pessoas que estao acima da media: ")
for cadadic in dados:
    if cadadic["idade"] > idade / len(dados):
        print("   ", end="")
        for k, v in cadadic.items():
            print("{} = {}; ".format(k, v), end="")
            if k == "idade":
                print()
print("<< ENCERRADO >>")
