"""ex075 - Analise de dados em uma tupla.
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posicao foi digitado o primeiro valor 3
C) Quais foram os numeros pares"""
nums = (int(input("Digite um numero: ")),
        int(input("Digite outro numero: ")),
        int(input("Digite mais um numero: ")),
        int(input("Digite o ultimo numero: ")))
print("Voce digitou os valores: {}".format(nums))
print("O valor 9 apareceu {} vezes.".format(nums.count(9)))
if 3 in nums:
    print("O valor 3 apareceu na {} posicao".format(nums.index(3) + 1))
else:
    print("O valor 3 nao foi digitado.")
print("Os valores pares digitados foram ", end="")
for num in nums:
    if num % 2 == 0:
        print("{} ".format(num), end="")
