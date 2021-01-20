"""ex096 - Funcao que calcula area
Faca um programa que tenha uma funcao chamada area(), que receba as dimensoes
de um terreno retangular (largura e comprimento) e mostre a area do terreno."""


def area(larg, compr):
    calc = larg * compr
    print("A area de um terreno {}x{} e de {}m2".format(larg, compr, calc))


# PROGRAMA PRINCIPAL
print("{:^22}".format("Controle de Terreno"))
print("-" * 22)

largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura, comprimento)
