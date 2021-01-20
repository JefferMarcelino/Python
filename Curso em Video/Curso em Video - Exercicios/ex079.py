"""ex079 - Valores unicos em uma lista
Crie um programa onde o usario possa digitar varios valores numericos e
cadastre-os em uma lista. Caso o numero ja exista la dentro, ele nao sera
adicionado. No final, serao exibidos todos os valores digitados, em ordem
crescente"""

nums = []
while True:
    num = int(input("Digite um valor: "))
    if num not in nums:
        nums.append(num)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Nao vou adicionar...")
    while True:
        r = str(input("Quer continuar? [S/N] ")).upper()[0]
        if r not in "SN":
            print("INVALIDO")
        else:
            break
    print("-=" * 30)
    if r == "N":
        break

print("-=" * 30)
print("Voce digitou os valores {}".format(sorted(nums)))
