"""ex081 - Extraindo dados de uma Lista
Crie um programa que vai ler varios numeros e colocar em uma lista. Depois, disso,
mostre:
A) Quantos numeros foram digitados
B) A lista de valores, ordenada de forma descrescente
C) Se o valor 5 foi digitado e esta ou nao na lista"""

nums = []
while True:
    nums.append(int(input("Digite um valor: ")))
    while True:
        r = str(input("Quer continuar? [S/N] ")).upper()[0]
        if r in "NS":
            break
        else:
            print("INVALIDO!")
    if r == "N":
        break
print("-=" * 30)
print("Voce digitou {} elementos".format(len(nums)))
print("Os valores em ordem descrescente sao {}".format(sorted(nums, reverse=True)))
if 5 in nums:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 nao foi encontrado na lista")
