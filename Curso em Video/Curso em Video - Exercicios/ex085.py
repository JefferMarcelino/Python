"""ex085 - Listas com pares e impares
Crie um programa onde o usario possa digitar sete valores numericos e cadastre-os
em uma lista unica que mantenha separdos os valores pares e impares. No final, mostre
os valores pares e impares em ordem crescente."""

Nums = [[], []]
for c in range(1, 8):
    v = int(input("Digite o {}o valor: ".format(c)))
    if v % 2 == 0:
        Nums[0].append(v)
    else:
        Nums[1].append(v)
print("-=" * 30)
Nums[0].sort()
Nums[1].sort()
print("Os valores pares digitados foram {}".format(Nums[0]))
print("Os valores impares digitados foram {}".format(Nums[1]))
