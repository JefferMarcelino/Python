"""ex092 - Cadastro de Trabalhador em Python
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade) em um dicionario se por acaso o CTPS for diferente de ZERO, o dicionario
recebera tambem o ano de contratacao e o salario. Calcule e acrescente, alem da idade,
com quantos anos a pessoa vai se aposentar."""

from datetime import datetime

dados = {}
dados["nome"] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
dados["idade"] = datetime.today().year - nasc
dados["ctps"] = int(input("Carteira de Trabalho (0 nao tem): "))
if dados["ctps"] != 0:
    dados["contratacao"] = int(input("Ano de Contratacao: "))
    dados["salario"] = float(input("Salario: "))
    dados["aposentadoria"] = dados["idade"] + (dados["contratacao"] + 35) - datetime.today().year

print("-=" * 30)
for k, v in dados.items():
    print("{} tem o valor {}".format(k, v))
