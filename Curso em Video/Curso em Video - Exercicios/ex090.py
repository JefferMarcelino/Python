"""ex090 - Dicionario em Python
Faca um programa que leia nome e media de um aluno, guardando tambem
a situacao em um dicionario. No final, mostre o conteudo da estrutura na tela."""

aluno = {}
aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input("Media do {}: ".format(aluno["nome"])))

if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
elif 5 <= aluno["media"] <7:
    aluno["situacao"] = "Recuperacao"
else:
    aluno["situacao"] = "Reprovado"
    
print("-=" * 30)

for k, v in aluno.items():
        print(" -{} e igual a {}".format(k, v))
